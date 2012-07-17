import unittest
from google.appengine.ext import testbed

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump
from minixsv import pyxsval as xsv

import XMLHelpers
from MainHandler import link_values
from DataModels import Person, Organization, Crisis, Link

class UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # First, create an instance of the Testbed class.
        cls.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        cls.testbed.activate()
        # Next, declare which service stubs you want to use.
        cls.testbed.init_datastore_v3_stub()

    @classmethod
    def tearDownClass(cls):
        #assert(False)
        cls.testbed.deactivate()

    # test class mutator for extracting links
    def test_crisisLink(self):
        
        link_query = "SELECT * FROM Link WHERE link_parent='haiti'"
        link = db.GqlQuery(link_query)

        dictionary = {}
        self.assert_(len(dictionary) == 0)
        link_values(dictionary, link)
        self.assert_(len(dictionary) != 0)

    def test_orgsLinks(self):
        
        link_query = "SELECT * FROM Link WHERE link_parent='wfp'"
        link = db.GqlQuery(link_query)

        dictionary = {}
        self.assert_(len(dictionary) == 0)
        link_values(dictionary, link)
        self.assert_(len(dictionary) != 0)

    def test_personLinks(self):
        
        link_query = "SELECT * FROM Link WHERE link_parent='aroche'"
        link = db.GqlQuery(link_query)

        dictionary = {}
        self.assert_(len(dictionary) == 0)
        link_values(dictionary, link)
        self.assert_(len(dictionary) != 0)

    def test_parse1(self):
        xml_file = open("test/test_parse1.xml", 'rb')
        XMLHelpers.parseXML(xml_file,1)
        temp = db.GqlQuery("SELECT * FROM Link")
        for i in temp:
            if i.link_type == "image":
                self.assert_(i.link_url == "https://www.google.com")
                break
        db.delete(db.Query())   

    def test_parse2(self):
        xml_file = open("test/test_parse2.xml", 'rb')
        XMLHelpers.parseXML(xml_file,1)
        temp = db.GqlQuery("SELECT * FROM Link")
        for i in temp:
            if i.link_type == "image":
                self.assert_(i.link_url == None)
                break
        db.delete(db.Query())        
        
    def test_parse3(self):
        xml_file = open("test/test_parse3.xml", 'rb')
        XMLHelpers.parseXML(xml_file,1)
        temp = db.GqlQuery("SELECT * FROM Link")
        for i in temp:
            if i.link_type == "image":
                self.assert_(i.link_url == None)
                break
        db.delete(db.Query())   
    
    def test_parse4(self):
        xml_file = open("test/test_parse4.xml", 'rb')
        XMLHelpers.parseXML(xml_file,0)
        temp = db.GqlQuery("SELECT * FROM Link")
        for i in temp:
            if i.link_type == "image":
                assert i.link_url == "aaaa"
                break
        db.delete(db.Query())
