import os
import unittest

import netCDF4
from lxml import etree
from petulantbear.netcdf_etree import parse_nc_dataset_as_etree, dataset2ncml


namespaces = {
    'x': 'http://www.unidata.ucar.edu/namespaces/netcdf/ncml-2.2'
}

class TestPb(unittest.TestCase):

    def setUp(self):
        self.file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test.nc'))

    def test_ncml_string(self):
        with netCDF4.Dataset(self.file) as ds:
            ncml = dataset2ncml(ds, url="file:{}".format(self.file))
            root = etree.fromstring(ncml)
            assert isinstance(root, etree._Element)

    def test_dimension(self):
        with netCDF4.Dataset(self.file, 'a') as ds:
            root = parse_nc_dataset_as_etree(ds)
            dim = root[0]
            assert dim.attrib['name'] == 'bad_name'

    def test_variable(self):
        with netCDF4.Dataset(self.file, 'a') as ds:
            root = parse_nc_dataset_as_etree(ds)
            vs = root.xpath('/x:netcdf/x:variable', namespaces=namespaces)
            assert len(vs) > 0
            for v in vs:
                assert v.attrib['name']

            v = root.xpath("x:variable[@name='var4']", namespaces=namespaces)[0]
            assert v.attrib['name'] == 'var4'

            v = root.xpath("x:variable[@name='var4']/x:attribute[@name='foo']", namespaces=namespaces)[0]
            assert v.attrib['name'] == 'foo'
            assert v.attrib['value'] == 'bar'

    def test_global(self):
        with netCDF4.Dataset(self.file, 'a') as ds:
            root = parse_nc_dataset_as_etree(ds)
            g = root.xpath("/x:netcdf/x:attribute[@name='foo']", namespaces=namespaces)[0]
            assert g.attrib['name'] == 'foo'
