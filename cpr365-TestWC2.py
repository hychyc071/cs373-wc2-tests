#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from StringIO import StringIO
from google.appengine.ext.webapp import Request
from google.appengine.ext.webapp import Response
from google.appengine.ext.webapp import RequestHandler
from main import Export
from main import Schema
from main import Import
from main import ImportSchema
from Models import *

class Test(unittest.TestCase):
    
    def testExternal1(self):
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.funny.com'
	siteActual = 'Funny Stuff'
	titleActual = 'Funny'
	descriptionActual = 'laughter in smiles'
	jiblet = External(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid == extActual.valid)
    
    def testExternal2(self):
	extActual = ExternalContent(valid = False)
	linkActual = 'http://www.coconuts.com'
	siteActual = 'Palm Stuff'
	titleActual = 'island trees'
	descriptionActual = 'California has palm trees lining the streets'
	jiblet = External(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid == extActual.valid)
    
    def testExternal3(self):
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.wallaby.com'
	siteActual = 'Funny wallaby'
	titleActual = 'Not a kangaroo'
	descriptionActual = 'jump jumpidy-jump-jump'
	jiblet = External(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid != False)
    
    def testImage1(self):
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.funny.com'
	siteActual = 'Funny Stuff'
	titleActual = 'Funny'
	descriptionActual = 'laughter in smiles'
	jiblet = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid == extActual.valid)
    
    def testImage2(self):
	extActual = ExternalContent(valid = False)
	linkActual = 'http://www.coconuts.com'
	siteActual = 'Palm Stuff'
	titleActual = 'island trees'
	descriptionActual = 'California has palm trees lining the streets'
	jiblet = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid == extActual.valid)
    
    def testImage3(self):
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.wallaby.com'
	siteActual = 'Funny wallaby'
	titleActual = 'Not a kangaroo'
	descriptionActual = 'jump jumpidy-jump-jump'
	jiblet = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid != False)
    
    def testVideo1(self):
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.funny.com'
	siteActual = 'Funny Stuff'
	titleActual = 'Funny'
	descriptionActual = 'laughter in smiles'
	jiblet = Video(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid == extActual.valid)
    
    def testVideo2(self):
	extActual = ExternalContent(valid = False)
	linkActual = 'http://www.coconuts.com'
	siteActual = 'Palm Stuff'
	titleActual = 'island trees'
	descriptionActual = 'California has palm trees lining the streets'
	jiblet = Video(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid == extActual.valid)
    
    def testVideo3(self):
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.wallaby.com'
	siteActual = 'Funny wallaby'
	titleActual = 'Not a kangaroo'
	descriptionActual = 'jump jumpidy-jump-jump'
	jiblet = Video(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid != False)
    
    def testSocial1(self):
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.funny.com'
	siteActual = 'Funny Stuff'
	titleActual = 'Funny'
	descriptionActual = 'laughter in smiles'
	jiblet = Social(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid == extActual.valid)
    
    def testSocial2(self):
	extActual = ExternalContent(valid = False)
	linkActual = 'http://www.coconuts.com'
	siteActual = 'Palm Stuff'
	titleActual = 'island trees'
	descriptionActual = 'California has palm trees lining the streets'
	jiblet = Social(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid == extActual.valid)
    
    def testSocial3(self):
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.wallaby.com'
	siteActual = 'Funny wallaby'
	titleActual = 'Not a kangaroo'
	descriptionActual = 'jump jumpidy-jump-jump'
	jiblet = Social(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	self.assert_(jiblet.link == linkActual)
	self.assert_(jiblet.site == siteActual)
	self.assert_(jiblet.description == descriptionActual)
	self.assert_(jiblet.title == titleActual)
	self.assert_(jiblet.ext.valid != False)
	
    def testExternalContent1(self):
	validActual = False
	intraCellularRadix = ExternalContent(valid = validActual)
	self.assert_(intraCellularRadix.valid == validActual)
	
    def testExternalContent1(self):
	validActual = True
	intraCellularRadix = ExternalContent(valid = validActual)
	self.assert_(intraCellularRadix.valid == validActual)
	
    def testExternalContent1(self):
	validActual = False
	intraCellularRadix = ExternalContent(valid = validActual)
	self.assert_(intraCellularRadix.valid != True)
	
    def testDate1(self):
	timeActual = '2:25:31pm'
	dayActual = '15'
	monthActual = 'March'
	yearActual = '1899'
	miscActual = 'walking'
	dateTacular = Date(time = timeActual, day = dayActual, month = monthActual, year = yearActual, misc = miscActual)
	self.assert_(dateTacular.time == timeActual)
	self.assert_(dateTacular.day == dayActual)
	self.assert_(dateTacular.month == monthActual)
	self.assert_(dateTacular.year == yearActual)
	self.assert_(dateTacular.misc == miscActual)
	
    def testDate2(self):
	timeActual = '12:25:31pm'
	dayActual = '5'
	monthActual = 'May'
	yearActual = '1900'
	miscActual = 'running'
	dateTacular = Date(time = timeActual, day = dayActual, month = monthActual, year = yearActual, misc = miscActual)
	self.assert_(dateTacular.time == timeActual)
	self.assert_(dateTacular.day == dayActual)
	self.assert_(dateTacular.month == monthActual)
	self.assert_(dateTacular.year == yearActual)
	self.assert_(dateTacular.misc == miscActual)
	
    def testDate3(self):
	timeActual = '9:25:31pm'
	dayActual = '2'
	monthActual = 'April'
	yearActual = '1901'
	miscActual = 'swimming'
	dateTacular = Date(time = timeActual, day = dayActual, month = monthActual, year = yearActual, misc = miscActual)
	self.assert_(dateTacular.time == timeActual)
	self.assert_(dateTacular.day == dayActual)
	self.assert_(dateTacular.month == monthActual)
	self.assert_(dateTacular.year == yearActual)
	self.assert_(dateTacular.misc == miscActual)
	
    def testLocation1(self):
	cityActual = 'Atlanta'
	regionActual = 'Georgia'
	countryActual = 'Zimbabwe'
	lokatie = Location(city = cityActual, region = regionActual, country = countryActual)
	self.assert_(lokatie.city == cityActual)
	self.assert_(lokatie.region == regionActual)
	self.assert_(lokatie.country == countryActual)
	
    def testLocation2(self):
	cityActual = 'Houston'
	regionActual = 'Texas'
	countryActual = 'Mongolia'
	lokatie = Location(city = cityActual, region = regionActual, country = countryActual)
	self.assert_(lokatie.city == cityActual)
	self.assert_(lokatie.region == regionActual)
	self.assert_(lokatie.country == countryActual)
	
    def testLocation3(self):
	cityActual = 'Austin'
	regionActual = 'Texas'
	countryActual = 'Easter Island'
	lokatie = Location(city = cityActual, region = regionActual, country = countryActual)
	self.assert_(lokatie.city == cityActual)
	self.assert_(lokatie.region == regionActual)
	self.assert_(lokatie.country == countryActual)
	
    def testContact1(self):
	phoneActual = '(512)555-9898'
	emailActual = 'tabBaybay@gmail.com'
	addressActual = '222 Bronson St.'
	cityActual = 'Bogota'
	stateActual = 'Arkansas'
	countryActual = 'USA'
	zipcodeActual = '78787'
	contactInMyEye = Contact(phone = phoneActual, email = emailActual, address = addressActual, city = cityActual, state = stateActual, country = countryActual, zipcode = zipcodeActual)
	self.assert_(contactInMyEye.phone = phoneActual)
	self.assert_(contactInMyEye.email = emailActual)
	self.assert_(contactInMyEye.address = addressActual)
	self.assert_(contactInMyEye.city = cityActual)
	self.assert_(contactInMyEye.state = stateActual)
	self.assert_(contactInMyEye.country = countryActual)
	self.assert_(contactInMyEye.zipcode = zipcodeActual)
	
    def testContact2(self):
	phoneActual = '(281)555-1111'
	emailActual = 'talkSanely@gmail.com'
	addressActual = '4242 Braker St.'
	cityActual = 'Detroit'
	stateActual = 'Illinois'
	countryActual = 'USA'
	zipcodeActual = '79999'
	contactInMyEye = Contact(phone = phoneActual, email = emailActual, address = addressActual, city = cityActual, state = stateActual, country = countryActual, zipcode = zipcodeActual)
	self.assert_(contactInMyEye.phone = phoneActual)
	self.assert_(contactInMyEye.email = emailActual)
	self.assert_(contactInMyEye.address = addressActual)
	self.assert_(contactInMyEye.city = cityActual)
	self.assert_(contactInMyEye.state = stateActual)
	self.assert_(contactInMyEye.country = countryActual)
	self.assert_(contactInMyEye.zipcode = zipcodeActual)
	
    def testContact3(self):
	phoneActual = '033(360)555-2222'
	emailActual = 'harryP@gmail.com'
	addressActual = '34 1/2 Hogwarts'
	cityActual = 'Mystic City'
	stateActual = 'Canteberry'
	countryActual = 'UK'
	zipcodeActual = 'S89856'
	contactInMyEye = Contact(phone = phoneActual, email = emailActual, address = addressActual, city = cityActual, state = stateActual, country = countryActual, zipcode = zipcodeActual)
	self.assert_(contactInMyEye.phone = phoneActual)
	self.assert_(contactInMyEye.email = emailActual)
	self.assert_(contactInMyEye.address = addressActual)
	self.assert_(contactInMyEye.city = cityActual)
	self.assert_(contactInMyEye.state = stateActual)
	self.assert_(contactInMyEye.country = countryActual)
	self.assert_(contactInMyEye.zipcode = zipcodeActual)
	
    def testEconomicImpact1(self):
	amountActual = 32000000
	currencyActual = 'Dollar'
	miscActual = 'Bigdisaster'
	econImpacto = EconImpact(amount = amountActual, currency = currencyActual, misc = miscActual)
	self.assert_(econImpacto.amount = amountActual)
	self.assert_(econImpacto.currency = currencyActual)
	self.assert_(econImpacto.misc = miscActual)
	
    def testEconomicImpact2(self):
	amountActual = 112000000
	currencyActual = 'Yen'
	miscActual = 'Bad Event'
	econImpacto = EconImpact(amount = amountActual, currency = currencyActual, misc = miscActual)
	self.assert_(econImpacto.amount = amountActual)
	self.assert_(econImpacto.currency = currencyActual)
	self.assert_(econImpacto.misc = miscActual)
	
    def testEconomicImpact3(self):
	amountActual = 76000000
	currencyActual = 'Dinar'
	miscActual = 'Not good'
	econImpacto = EconImpact(amount = amountActual, currency = currencyActual, misc = miscActual)
	self.assert_(econImpacto.amount = amountActual)
	self.assert_(econImpacto.currency = currencyActual)
	self.assert_(econImpacto.misc = miscActual)
	
    def testHumanImpact1(self):
	deathsActual = 555555
	displacedActual = 4000000
	injuredActual = 28000
	missing = 5444000
	miscActual = 'large numbers'
	humanImpacto = HumanImpact(deaths = deathsActual, displaced = displacedActual, injured = injuredActual, missing = missingActual, misc = miscActual)
	self.assert_(humanImpacto.deaths == deathsActual)
	self.assert_(humanImpacto.displaced == displacedActual)
	self.assert_(humanImpacto.injured == injuredActual)
	self.assert_(humanImpacto.missing == missingActual)
	self.assert_(humanImpacto.misc == miscActual)
	
    def testHumanImpact2(self):
	deathsActual = 67000
	displacedActual = 600000
	injuredActual = 55000
	missingActual = 3232000
	miscActual = 'man!!'
	humanImpacto = HumanImpact(deaths = deathsActual, displaced = displacedActual, injured = injuredActual, missing = missingActual, misc = miscActual)
	self.assert_(humanImpacto.deaths == deathsActual)
	self.assert_(humanImpacto.displaced == displacedActual)
	self.assert_(humanImpacto.injured == injuredActual)
	self.assert_(humanImpacto.missing == missingActual)
	self.assert_(humanImpacto.misc == miscActual)
	
    def testHumanImpact3(self):
	deathsActual = 9800000
	displacedActual = 8800000
	injuredActual = 87000
	missingActual = 111000
	miscActual = 'oi!!'
	humanImpacto = HumanImpact(deaths = deathsActual, displaced = displacedActual, injured = injuredActual, missing = missingActual, misc = miscActual)
	self.assert_(humanImpacto.deaths == deathsActual)
	self.assert_(humanImpacto.displaced == displacedActual)
	self.assert_(humanImpacto.injured == injuredActual)
	self.assert_(humanImpacto.missing == missingActual)
	self.assert_(humanImpacto.misc == miscActual)
	
	
    def testPerson1(self) :
	nameActual = 'Anita Sanchez'
	type_Actual = 'Director'
	nationalityActual = 'Japanese'
	biographyActual = 'Anita spent her early childhood in papua new Guinea but then moved to Tokyo at the age of 6'
	timeActual = '2:25:31pm'
	dayActual = '15'
	monthActual = 'March'
	yearActual = '1899'
	miscActual = 'walking'
	birthdayActual = Date(time = timeActual, day = dayActual, month = monthActual, year = yearActual, misc = miscActual)
	miscActual = 'she got here phD in philosophy at the age 16'
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.funny.com'
	siteActual = 'Funny Stuff'
	titleActual = 'Funny'
	descriptionActual = 'laughter in smiles'
	primaryImageActual = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	externalContentActual = extActual
	relatedCrisesActual = ['flood', 'food shortage']
	relatedOrganizationsActual = ['Red Cross', 'PETA']
	stored_onActual = db.DateTimeProperty(auto_now_add = True)
	personickle = Person(name = nameActual, type_ = type_Actual, nationality = nationalityActual, biography = biographyActual, birthday = birthdayActual, misc = miscActual, primaryImage = primaryImageActual, externalContent = externalContentActual, relatedCrises = relatedCrisesActual, relatedOrganizations = relatedOrganizationsActual, stored_on = stored_onActual)
	self.assert_(peronickle.name == nameActual)
	self.assert_(peronickle.type_ == type_Actual)
	self.assert_(peronickle.nationality == nationalityActual)
	self.assert_(peronickle.biography == biographyActual)
	self.assert_(peronickl
	deathsActual = 555555
	displacedActual = 4000000
	injuredActual = 28000
	missing = 5444000
	miscActual = 'large numbers'
	humanImpacto = HumanImpact(deaths = deathsActual, displaced = displacedActual, injured = injuredActual, missing = missingActual, misc = miscActual)e.birthday == birthdayActual)
	self.assert_(peronickle.misc == miscActual)
	self.assert_(peronickle.primaryImage == primaryImageActual)
	self.assert_(peronickle.externalContent == externalContentActual)
	self.assert_(peronickle.relatedCrises == relatedCrisesActual)
	self.assert_(peronickle.relatedOrganizations == relatedOrganizationsActual)
	self.assert_(peronickle.stored_on == stored_onActual)
	
	
    def testPerson2(self) :
	nameActual = 'George Clooney'
	type_Actual = 'Vice President'
	nationalityActual = 'American'
	biographyActual = 'George was curious and ran a lemonade stand until he was 27'
	timeActual = '12:25:31pm'
	dayActual = '5'
	monthActual = 'May'
	yearActual = '1900'
	miscActual = 'running'
	birthdayActual = Date(time = timeActual, day = dayActual, month = monthActual, year = yearActual, misc = miscActual)
	miscActual = 'He loves potatoes'
	extActual = ExternalContent(valid = False)
	linkActual = 'http://www.coconuts.com'
	siteActual = 'Palm Stuff'
	titleActual = 'island trees'
	descriptionActual = 'California has palm trees lining the streets'
	primaryImageActual = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	externalContentActual = extActual
	relatedCrisesActual = ['darfur', 'katrina']
	relatedOrganizationsActual = ['World Health Organization', 'National Education Grant']
	stored_onActual = db.DateTimeProperty(auto_now_add = True)
	personickle = Person(name = nameActual, type_ = type_Actual, nationality = nationalityActual, biography = biographyActual, birthday = birthdayActual, misc = miscActual, primaryImage = primaryImageActual, externalContent = externalContentActual, relatedCrises = relatedCrisesActual, relatedOrganizations = relatedOrganizationsActual, stored_on = stored_onActual)
	self.assert_(peronickle.name == nameActual)
	self.assert_(peronickle.type_ == type_Actual)
	self.assert_(peronickle.nationality == nationalityActual)
	self.assert_(peronickle.biography == biographyActual)
	self.assert_(peronickle.birthday == birthdayActual)
	self.assert_(peronickle.misc == miscActual)
	self.assert_(peronickle.primaryImage == primaryImageActual)
	self.assert_(peronickle.externalContent == externalContentActual)
	self.assert_(peronickle.relatedCrises == relatedCrisesActual)
	self.assert_(peronickle.relatedOrganizations == relatedOrganizationsActual)
	self.assert_(peronickle.stored_on == stored_onActual)
	
	
    def testPerson3(self) :
	nameActual = 'Brad Pitt'
	type_Actual = 'Public Relations'
	nationalityActual = 'American'
	biographyActual = 'He was raised in Louisiana, his birth name was LeStat'
	timeActual = '9:25:31pm'
	dayActual = '2'
	monthActual = 'April'
	yearActual = '1901'
	miscActual = 'swimming'
	birthdayActual = Date(time = timeActual, day = dayActual, month = monthActual, year = yearActual, misc = miscActual)
	miscActual = 'he could talk at the age of 7'
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.wallaby.com'
	siteActual = 'Funny wallaby'
	titleActual = 'Not a kangaroo'
	descriptionActual = 'jump jumpidy-jump-jump'
	primaryImageActual = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	externalContentActual = extActual
	relatedCrisesActual = ['drought', 'endangered animals']
	relatedOrganizationsActual = ['Keep the Wetlands Wet Organization', 'Wildlife Foundation']
	stored_onActual = db.DateTimeProperty(auto_now_add = True)
	personickle = Person(name = nameActual, type_ = type_Actual, nationality = nationalityActual, biography = biographyActual, birthday = birthdayActual, misc = miscActual, primaryImage = primaryImageActual, externalContent = externalContentActual, relatedCrises = relatedCrisesActual, relatedOrganizations = relatedOrganizationsActual, stored_on = stored_onActual)
	self.assert_(peronickle.name == nameActual)
	self.assert_(peronickle.type_ == type_Actual)
	self.assert_(peronickle.nationality == nationalityActual)
	self.assert_(peronickle.biography == biographyActual)
	self.assert_(peronickle.birthday == birthdayActual)
	self.assert_(peronickle.misc == miscActual)
	self.assert_(peronickle.primaryImage == primaryImageActual)
	self.assert_(peronickle.externalContent == externalContentActual)
	self.assert_(peronickle.relatedCrises == relatedCrisesActual)
	self.assert_(peronickle.relatedOrganizations == relatedOrganizationsActual)
	self.assert_(peronickle.stored_on == stored_onActual)
	
	
    def testCrisis1(self) :
	nameActual = 'Tunguska Explosion'
	historyActual = 'only a few siberian tribes lived in the area'
	helpActual = 'you can donate wildlife seeds and aerial drops'
	resourcesActual = 'water, canned goods'
	type_Actual = 'Meteor Impact'
	timeForDateActual = '2:25:31pm'
	dayActual = '15'
	monthActual = 'March'
	yearActual = '1899'
	miscActual = 'walking'
	timeActual = Date(time = timeForDateActual, day = dayActual, month = monthActual, year = yearActual, misc = miscActual)
	cityActual = 'Atlanta'
	regionActual = 'Georgia'
	countryActual = 'Zimbabwe'
	locationActual = Location(city = cityActual, region = regionActual, country = countryActual)
	deathsActual = 555555
	displacedActual = 4000000
	injuredActual = 28000
	missing = 5444000
	miscActual = 'large numbers'
	humanImpactActual = HumanImpact(deaths = deathsActual, displaced = displacedActual, injured = injuredActual, missing = missingActual, misc = miscActual)
	amountActual = 32000000
	currencyActual = 'Dollar'
	miscActual = 'Bigdisaster'
	econImpactActual = EconImpact(amount = amountActual, currency = currencyActual, misc = miscActual)
	miscActual = 'Trees were leveled radiating outward from impact site'
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.funny.com'
	siteActual = 'Funny Stuff'
	titleActual = 'Funny'
	descriptionActual = 'laughter in smiles'
	primaryImageActual = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	externalContentActual = extActual
	relatedPersonsActual = ['Brad Pitt', 'George Clooney']
	relatedOrganizationsActual = ['Red Cross', 'PETA']
	stored_onActual = db.DateTimeProperty(auto_now_add = True)
	crisisBigg = Crisis(name = nameActual, history = historyActual, help = helpActual, resources = resourcesActual, type_ = type_Actual, time = timeActual, location = locationActual, humanImpact = humanImpactActual, econImpact = econImpactActual,  misc = miscActual, primaryImage = primaryImageActual, externalContent = externalContentActual, relatedPersons = relatedPersonsActual, relatedOrganizations = relatedOrganizationsActual, stored_on = stored_onActual)
	self.assert_(crisisBigg.name == nameActual)
	self.assert_(crisisBigg.history == historyActual)
	self.assert_(crisisBigg.help == helpActual)
	self.assert_(crisisBigg.resources == resourcesActual)
	self.assert_(crisisBigg.type_ == type_Actual)
	self.assert_(crisisBigg.time == timeActual)
	self.assert_(crisisBigg.location == locationActual)
	self.assert_(crisisBigg.humanImpact == humanImpactActual)
	self.assert_(crisisBigg.econImpact == econImpactActual)
	self.assert_(crisisBigg.misc == miscActual)
	self.assert_(crisisBigg.primaryImage == primaryImageActual)
	self.assert_(crisisBigg.externalContent == externalContentActual)
	self.assert_(crisisBigg.relatedPersons == relatedPersonsActual)
	self.assert_(crisisBigg.relatedOrganizations == relatedOrganizationsActual)
	self.assert_(crisisBigg.stored_on == stored_onActual)
	
	
    def testCrisis2(self) :
	nameActual = 'Atlantis flood'
	historyActual = 'had 100ft high cliffs, was located in present day Meditaranean Sea'
	helpActual = 'you can donate floatillas and aerial drops'
	resourcesActual = 'clothes lines, water, canned goods'
	type_Actual = 'big wave sunamee'
	timeActual = '12:25:31pm'
	dayActual = '5'
	monthActual = 'May'
	yearActual = '1900'
	miscActual = 'running'
	timeActual = Date(time = timeForDateActual, day = dayActual, month = monthActual, year = yearActual, misc = miscActual)
	cityActual = 'Atlantis'
	regionActual = 'Meditaranean'
	countryActual = 'Atlantia'
	locationActual = Location(city = cityActual, region = regionActual, country = countryActual)
	deathsActual = 67000
	displacedActual = 600000
	injuredActual = 55000
	missingActual = 3232000
	miscActual = 'man!!'
	humanImpactActual = HumanImpact(deaths = deathsActual, displaced = displacedActual, injured = injuredActual, missing = missingActual, misc = miscActual)
	amountActual = 112000000
	currencyActual = 'Yen'
	miscActual = 'Bad Event'
	econImpactActual = EconImpact(amount = amountActual, currency = currencyActual, misc = miscActual)
	miscActual = 'the city was washed into the sea'
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.coconuts.com'
	siteActual = 'Palm Stuff'
	titleActual = 'island trees'
	descriptionActual = 'California has palm trees lining the streets'
	primaryImageActual = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	externalContentActual = extActual
	relatedPersonsActual = ['Debra Winger', 'John Voight']
	relatedOrganizationsActual = ['Coleman Foundation', 'Bill Gates Foundation']
	stored_onActual = db.DateTimeProperty(auto_now_add = True)
	crisisBigg = Crisis(name = nameActual, history = historyActual, help = helpActual, resources = resourcesActual, type_ = type_Actual, time = timeActual, location = locationActual, humanImpact = humanImpactActual, econImpact = econImpactActual,  misc = miscActual, primaryImage = primaryImageActual, externalContent = externalContentActual, relatedPersons = relatedPersonsActual, relatedOrganizations = relatedOrganizationsActual, stored_on = stored_onActual)
	self.assert_(crisisBigg.name == nameActual)
	self.assert_(crisisBigg.history == historyActual)
	self.assert_(crisisBigg.help == helpActual)
	self.assert_(crisisBigg.resources == resourcesActual)
	self.assert_(crisisBigg.type_ == type_Actual)
	self.assert_(crisisBigg.time == timeActual)
	self.assert_(crisisBigg.location == locationActual)
	self.assert_(crisisBigg.humanImpact == humanImpactActual)
	self.assert_(crisisBigg.econImpact == econImpactActual)
	self.assert_(crisisBigg.misc == miscActual)
	self.assert_(crisisBigg.primaryImage == primaryImageActual)
	self.assert_(crisisBigg.externalContent == externalContentActual)
	self.assert_(crisisBigg.relatedPersons == relatedPersonsActual)
	self.assert_(crisisBigg.relatedOrganizations == relatedOrganizationsActual)
	self.assert_(crisisBigg.stored_on == stored_onActual)
	
	
    def testCrisis3(self) :
	nameActual = 'Mount St. Helena Explosion'
	historyActual = 'The vulcano never exploded before in recorded history'
	helpActual = 'you can donate wildlife seeds and aerial drops'
	resourcesActual = 'shovels, water, clean clothing of all sizes, canned goods'
	type_Actual = 'Vulcano Erruption'
	timeActual = '9:25:31pm'
	dayActual = '2'
	monthActual = 'April'
	yearActual = '1901'
	miscActual = 'swimming'
	timeActual = Date(time = timeForDateActual, day = dayActual, month = monthActual, year = yearActual, misc = miscActual)
	cityActual = 'Helena'
	regionActual = 'Montana'
	countryActual = 'USA'
	locationActual = Location(city = cityActual, region = regionActual, country = countryActual)
	deathsActual = 9800000
	displacedActual = 8800000
	injuredActual = 87000
	missingActual = 111000
	miscActual = 'oi!!'
	humanImpactActual = HumanImpact(deaths = deathsActual, displaced = displacedActual, injured = injuredActual, missing = missingActual, misc = miscActual)
	amountActual = 76000000
	currencyActual = 'Dolar'
	miscActual = 'Not good'
	econImpactActual = EconImpact(amount = amountActual, currency = currencyActual, misc = miscActual)
	miscActual = 'Trees were leveled radiating outward from impact site like the Tunguskan blast'
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.wallaby.com'
	siteActual = 'Funny wallaby'
	titleActual = 'Not a kangaroo'
	descriptionActual = 'jump jumpidy-jump-jump'
	primaryImageActual = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	externalContentActual = extActual
	relatedPersonsActual = ['Scarlet Johanson', 'Emerald Legosi']
	relatedOrganizationsActual = ['Montana National Guard', 'Lenny Kravits Organization']
	stored_onActual = db.DateTimeProperty(auto_now_add = True)
	crisisBigg = Crisis(name = nameActual, history = historyActual, help = helpActual, resources = resourcesActual, type_ = type_Actual, time = timeActual, location = locationActual, humanImpact = humanImpactActual, econImpact = econImpactActual,  misc = miscActual, primaryImage = primaryImageActual, externalContent = externalContentActual, relatedPersons = relatedPersonsActual, relatedOrganizations = relatedOrganizationsActual, stored_on = stored_onActual)
	self.assert_(crisisBigg.name == nameActual)
	self.assert_(crisisBigg.history == historyActual)
	self.assert_(crisisBigg.help == helpActual)
	self.assert_(crisisBigg.resources == resourcesActual)
	self.assert_(crisisBigg.type_ == type_Actual)
	self.assert_(crisisBigg.time == timeActual)
	self.assert_(crisisBigg.location == locationActual)
	self.assert_(crisisBigg.humanImpact == humanImpactActual)
	self.assert_(crisisBigg.econImpact == econImpactActual)
	self.assert_(crisisBigg.misc == miscActual)
	self.assert_(crisisBigg.primaryImage == primaryImageActual)
	self.assert_(crisisBigg.externalContent == externalContentActual)
	self.assert_(crisisBigg.relatedPersons == relatedPersonsActual)
	self.assert_(crisisBigg.relatedOrganizations == relatedOrganizationsActual)
	self.assert_(crisisBigg.stored_on == stored_onActual)
	
	
    def testOrganization1(self) :
	nameActual = 'Red Cross'
	historyActual = 'established in 1889'
	type_Actual = 'General purpose humanitarian aid'
	cityActual = 'Atlanta'
	regionActual = 'Georgia'
	countryActual = 'Zimbabwe'
	locationActual = Location(city = cityActual, region = regionActual, country = countryActual)
	phoneActual = '(512)555-9898'
	emailActual = 'tabBaybay@gmail.com'
	addressActual = '222 Bronson St.'
	cityActual = 'Bogota'
	stateActual = 'Arkansas'
	countryActual = 'USA'
	zipcodeActual = '78787'
	contactActual = Contact(phone = phoneActual, email = emailActual, address = addressActual, city = cityActual, state = stateActual, country = countryActual, zipcode = zipcodeActual)
	miscActual = 'Served in WWI and WWII'
	linkActual = 'http://www.redCrossing.com'
	siteActual = 'Red Cross'
	titleActual = 'Being Helpful'
	descriptionActual = 'give a hand when possible'
	primaryImageActual = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	extActual = ExternalContent(valid = True)
	externalContentActual = extActual
	relatedCrisesActual = ['flood', 'food shortage']
	relatedPersonsActual = ['Brad Pitt', 'George Clooney']
	stored_onActual = db.DateTimeProperty(auto_now_add = True)
	organizationBigg = Organization(name = nameActual, history = historyActual, type_ = type_Actual, location = locationActual, contact = contactActual, misc = miscActual, primaryImage = primaryImageActual, externalContent = externalContentActual, relatedPersons = relatedPersonsActual, relatedCrises = relatedCrisesActual, stored_on = stored_onActual)
	self.assert_(organizationBigg.name == nameActual)
	self.assert_(organizationBigg.history == historyActual)
	self.assert_(organizationBigg.contact == contactActual)
	self.assert_(organizationBigg.type_ == type_Actual)
	self.assert_(organizationBigg.location == locationActual)
	self.assert_(organizationBigg.misc == miscActual)
	self.assert_(organizationBigg.primaryImage == primaryImageActual)
	self.assert_(organizationBigg.externalContent == externalContentActual)
	self.assert_(organizationBigg.relatedPersons == relatedPersonsActual)
	self.assert_(organizationBigg.relatedCrises == relatedCrisesActual)
	self.assert_(organizationBigg.stored_on == stored_onActual)
	
	
    def testOrganization2(self) :
	nameActual = 'World Health Organization'
	historyActual = 'founder was Eric Binks'
	type_Actual = 'Health and humanitarian aid'
	cityActual = 'Atlantis'
	regionActual = 'Meditaranean'
	countryActual = 'Atlantia'
	locationActual = Location(city = cityActual, region = regionActual, country = countryActual)
	phoneActual = '(281)555-1111'
	emailActual = 'talkSanely@gmail.com'
	addressActual = '4242 Braker St.'
	cityActual = 'Detroit'
	stateActual = 'Illinois'
	countryActual = 'USA'
	zipcodeActual = '79999'
	contactActual = Contact(phone = phoneActual, email = emailActual, address = addressActual, city = cityActual, state = stateActual, country = countryActual, zipcode = zipcodeActual)
	linkActual = 'http://www.coconuts.com'
	siteActual = 'Palm Stuff'
	titleActual = 'island trees'
	descriptionActual = 'California has palm trees lining the streets'
	primaryImageActual = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	extActual = ExternalContent(valid = True)
	externalContentActual = extActual
	relatedCrisesActual = ['smallpox pandemic', 'ethiopian famine']
	relatedPersonsActual = ['Debra Winger', 'John Voight']
	stored_onActual = db.DateTimeProperty(auto_now_add = True)
	organizationBigg = Organization(name = nameActual, history = historyActual, type_ = type_Actual, location = locationActual, contact = contactActual, misc = miscActual, primaryImage = primaryImageActual, externalContent = externalContentActual, relatedPersons = relatedPersonsActual, relatedCrises = relatedCrisesActual, stored_on = stored_onActual)
	self.assert_(organizationBigg.name == nameActual)
	self.assert_(organizationBigg.history == historyActual)
	self.assert_(organizationBigg.contact == contactActual)
	self.assert_(organizationBigg.type_ == type_Actual)
	self.assert_(organizationBigg.location == locationActual)
	self.assert_(organizationBigg.misc == miscActual)
	self.assert_(organizationBigg.primaryImage == primaryImageActual)
	self.assert_(organizationBigg.externalContent == externalContentActual)
	self.assert_(organizationBigg.relatedPersons == relatedPersonsActual)
	self.assert_(organizationBigg.relatedCrises == relatedCrisesActual)
	self.assert_(organizationBigg.stored_on == stored_onActual)
      
      
      
	nameActual = 'Atlantis flood'
	historyActual = 'had 100ft high cliffs, was located in present day Meditaranean Sea'
	helpActual = 'you can donate floatillas and aerial drops'
	resourcesActual = 'clothes lines, water, canned goods'
	type_Actual = 'big wave sunamee'
	timeActual = '12:25:31pm'
	dayActual = '5'
	monthActual = 'May'
	yearActual = '1900'
	miscActual = 'running'
	timeActual = Date(time = timeForDateActual, day = dayActual, month = monthActual, year = yearActual, misc = miscActual)
	cityActual = 'Atlantis'
	regionActual = 'Meditaranean'
	countryActual = 'Atlantia'
	locationActual = Location(city = cityActual, region = regionActual, country = countryActual)
	deathsActual = 67000
	displacedActual = 600000
	injuredActual = 55000
	missingActual = 3232000
	miscActual = 'man!!'
	humanImpactActual = HumanImpact(deaths = deathsActual, displaced = displacedActual, injured = injuredActual, missing = missingActual, misc = miscActual)
	amountActual = 112000000
	currencyActual = 'Yen'
	miscActual = 'Bad Event'
	econImpactActual = EconImpact(amount = amountActual, currency = currencyActual, misc = miscActual)
	miscActual = 'the city was washed into the sea'
	extActual = ExternalContent(valid = True)
	linkActual = 'http://www.coconuts.com'
	siteActual = 'Palm Stuff'
	titleActual = 'island trees'
	descriptionActual = 'California has palm trees lining the streets'
	primaryImageActual = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	externalContentActual = extActual
	relatedPersonsActual = ['Debra Winger', 'John Voight']
	relatedOrganizationsActual = ['Coleman Foundation', 'Bill Gates Foundation']
	stored_onActual = db.DateTimeProperty(auto_now_add = True)
	crisisBigg = Crisis(name = nameActual, history = historyActual, help = helpActual, resources = resourcesActual, type_ = type_Actual, time = timeActual, location = locationActual, humanImpact = humanImpactActual, econImpact = econImpactActual,  misc = miscActual, primaryImage = primaryImageActual, externalContent = externalContentActual, relatedPersons = relatedPersonsActual, relatedOrganizations = relatedOrganizationsActual, stored_on = stored_onActual)
	self.assert_(crisisBigg.name == nameActual)
	self.assert_(crisisBigg.history == historyActual)
	self.assert_(crisisBigg.help == helpActual)
	self.assert_(crisisBigg.resources == resourcesActual)
	self.assert_(crisisBigg.type_ == type_Actual)
	self.assert_(crisisBigg.time == timeActual)
	self.assert_(crisisBigg.location == locationActual)
	self.assert_(crisisBigg.humanImpact == humanImpactActual)
	self.assert_(crisisBigg.econImpact == econImpactActual)
	self.assert_(crisisBigg.misc == miscActual)
	self.assert_(crisisBigg.primaryImage == primaryImageActual)
	self.assert_(crisisBigg.externalContent == externalContentActual)
	self.assert_(crisisBigg.relatedPersons == relatedPersonsActual)
	self.assert_(crisisBigg.relatedOrganizations == relatedOrganizationsActual)
	self.assert_(crisisBigg.stored_on == stored_onActual)
	
	
    def testOrganization3(self) :
	nameActual = 'International Wildlife Foundation'
	historyActual = 'It was established by Huckleberry Finn'
	type_Actual = 'Global Environmental Protection'
	cityActual = 'Helena'
	regionActual = 'Montana'
	countryActual = 'USA'
	locationActual = Location(city = cityActual, region = regionActual, country = countryActual)
	phoneActual = '033(360)555-2222'
	emailActual = 'harryP@gmail.com'
	addressActual = '34 1/2 Hogwarts'
	cityActual = 'Mystic City'
	stateActual = 'Canteberry'
	countryActual = 'UK'
	zipcodeActual = 'S89856'
	contactActual = Contact(phone = phoneActual, email = emailActual, address = addressActual, city = cityActual, state = stateActual, country = countryActual, zipcode = zipcodeActual)
	linkActual = 'http://www.wallaby.com'
	siteActual = 'Funny wallaby'
	titleActual = 'Not a kangaroo'
	descriptionActual = 'jump jumpidy-jump-jump'
	primaryImageActual = Image(link = linkActual, site = siteActual, title = titleActual, description = descriptionActual, ext = extActual)
	extActual = ExternalContent(valid = True)
	externalContentActual = extActual
	relatedCrisesActual = ['endagered big-cats', 'protect the Ice-Caps']
	relatedPersonsActual = ['Scarlet Johanson', 'Emerald Legosi']
	stored_onActual = db.DateTimeProperty(auto_now_add = True)
	organizationBigg = Organization(name = nameActual, history = historyActual, type_ = type_Actual, location = locationActual, contact = contactActual, misc = miscActual, primaryImage = primaryImageActual, externalContent = externalContentActual, relatedPersons = relatedPersonsActual, relatedCrises = relatedCrisesActual, stored_on = stored_onActual)
	self.assert_(organizationBigg.name == nameActual)
	self.assert_(organizationBigg.history == historyActual)
	self.assert_(organizationBigg.contact == contactActual)
	self.assert_(organizationBigg.type_ == type_Actual)
	self.assert_(organizationBigg.location == locationActual)
	self.assert_(organizationBigg.misc == miscActual)
	self.assert_(organizationBigg.primaryImage == primaryImageActual)
	self.assert_(organizationBigg.externalContent == externalContentActual)
	self.assert_(organizationBigg.relatedPersons == relatedPersonsActual)
	self.assert_(organizationBigg.relatedCrises == relatedCrisesActual)
	self.assert_(organizationBigg.stored_on == stored_onActual)
	
    def test_Schema1(self):
        j = Schema(schema = 'why the hell-o')
        self.assert_(j.schema == 'why the hell-o')
       
    def test_Schema2(self):
        j = Schema(schema = 'fleece the sheep')
        self.assert_(j.schema == 'fleece the sheep')
       
    def test_Schema3(self):
        j = Schema(schema = 'the rabbits in the hat')
        self.assert_(j.schema == 'the rabbits in the hat')
       
    def test_Import_post(self):
        handler = Import()
        self.assert_(issubclass(type(handler), RequestHandler))
