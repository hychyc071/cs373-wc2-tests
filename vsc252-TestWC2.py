import unittest
from test import test_support
from WC2 import *

class MyTestCase1(unittest.TestCase):

	def test_XMLNode_id(self):
		node = XMLNode(xml_id = 'abc')
		self.assertTrue(node.xml_id == 'abc')

	def test_XMLNode_text(self):
		node = XMLNode(xml_text = 'testing')
		self.assertTrue(node.xml_text == 'testing')

	def test_XMLNode_attr(self):
		node = XMLNode(xml_attr = ['abc', 'def'])
		self.assertTrue(node.xml_attr[0] == 'abc')

	def test_XMLNode_i(self):
		node = XMLNode(xml_i = 1)
		self.assertTrue(node.xml_i == 1)

	def test_Media_site(self):
		model = Media(site = "YouTube")
		self.assertTrue(model.site == "YouTube")

	def test_Media_title(self):
		model = Media(title = "Avian Flu: The H5N1 virus")
		self.assertTrue(model.title == "Avian Flu: The H5N1 virus")

	def test_Media_url(self):
		model = Media(url = "http://www.youtube.com/embed/uHPBdjCFDkE")
		self.assertTrue(model.url == "http://www.youtube.com/embed/uHPBdjCFDkE")

	def test_Media_description(self):
		model = Media(description = "A veterinarian explains what exactly the H5N1 Avian Flu virus is about.")
		self.assertTrue(model.description == "A veterinarian explains what exactly the H5N1 Avian Flu virus is about.")

	def test_Crisis_attr(self):
		model = Crisis(identifier = "RwandaGen", name = "Rwanda Genocide", info_type = "Murder", misc = "Mass genocide of people.", location_city = "Santiago", location_region = "New York", location_country = "Rwanda", time = "15:20", day = 31, month = 03, year = 1948, time_misc = "20th century", history = "There had always been heavy ethnic tension between the majority Hutu people and the Tutsis in Rwanda since the country's establishment.", help = "Awareness", resources = "", human_impact_injured= 344, human_impact_deaths = 111, human_impact_missing = 19999, human_impact_displaced = 1222, economic_impact_amount = 10000000, economic_impact_currency = "US$", economic_impact_misc = "10000")
		self.assertTrue(model.identifier == "RwandaGen")
		self.assertTrue(model.name == "Rwanda Genocide")
		self.assertTrue(model.info_type == "Murder")
		self.assertTrue(model.misc == "Mass genocide of people.")
		self.assertTrue(model.location_city == "Santiago")
		self.assertTrue(model.location_region == "New York")
		self.assertTrue(model.location_country == "Rwanda")
		self.assertTrue(model.time == "15:20")
		self.assertTrue(model.day == 31)
		self.assertTrue(model.month == 03)
		self.assertTrue(model.year == 1948)
		self.assertTrue(model.time_misc == "20th century")
		self.assertTrue(model.history == "There had always been heavy ethnic tension between the majority Hutu people and the Tutsis in Rwanda since the country's establishment.")
		self.assertTrue(model.help == "Awareness")
		self.assertTrue(model.resources == "")
		self.assertTrue(model.human_impact_injured == 344)
		self.assertTrue(model.human_impact_deaths == 111)
		self.assertTrue(model.human_impact_missing  == 19999)
		self.assertTrue(model.human_impact_displaced == 1222)
		self.assertTrue(model.economic_impact_amount == 10000000)
		self.assertTrue(model.economic_impact_currency == "US$")
		self.assertTrue(model.economic_impact_misc == "10000")

	def test_Crisis_primaryImage(self):
		img = Media(site = "istofworld.com", title = "Chilean Road After Earthquake", url = "http://www.listsofworld.com/wp-content/uploads/2011/12/Largest-earthquake-2010-Chile-Earthquake.jpg", description = "Road in Chile")
		model = Crisis()
		model.primaryImage = img
		self.assertTrue(model.primaryImage.site == "istofworld.com")
		self.assertTrue(model.primaryImage.title == "Chilean Road After Earthquake")
		self.assertTrue(model.primaryImage.url =="http://www.listsofworld.com/wp-content/uploads/2011/12/Largest-earthquake-2010-Chile-Earthquake.jpg")
		self.assertTrue(model.primaryImage.description == "Road in Chile")


	def test_Crisis_images(self):
		img = Media(site = "Wikipedia", title = "Specific Areas Affected", url = "http://upload.wikimedia.org/wikipedia/commons/6/68/2010_Maule_earthquake_intensity_USGS.jpg", description = "Specifies the regions in the country of Chile and the intensity that each one got hit with.")
		img.put()
		imglist = [img.key()]
		model = Crisis()
		model.images = imglist
		self.assertTrue(db.get(model.images[0]).site == "Wikipedia")
		self.assertTrue(db.get(model.images[0]).title == "Specific Areas Affected")
		self.assertTrue(db.get(model.images[0]).url == "http://upload.wikimedia.org/wikipedia/commons/6/68/2010_Maule_earthquake_intensity_USGS.jpg")
		self.assertTrue(db.get(model.images[0]).description == "Specifies the regions in the country of Chile and the intensity that each one got hit with.")

	def test_Crisis_videos(self):
		vid = Media(site = "YouTube", title = "The 2010 Great Chile Earthquake and its Aftershocks", url = "http://www.youtube.com/embed/kr44Q_b_CX4", description = "Animation that shows the seismic history of the Earthquake that hit Chile.")
		vid.put()
		vidlist = [vid.key()]
		model = Crisis()
		model.videos = vidlist
		self.assertTrue(db.get(model.videos[0]).site == "YouTube")
		self.assertTrue(db.get(model.videos[0]).title == "The 2010 Great Chile Earthquake and its Aftershocks")
		self.assertTrue(db.get(model.videos[0]).url == "http://www.youtube.com/embed/kr44Q_b_CX4")
		self.assertTrue(db.get(model.videos[0]).description == "Animation that shows the seismic history of the Earthquake that hit Chile.")

	def test_Crisis_socials(self):
		soc = Media(site = "Facebook", title = "Chile Earthquake", url = "https://www.facebook.com/chileearthquakeupdate?filter=3", description = "Coverage of the events of the Chilean Earthquake as they unfolded.")
		soc.put()
		soclist = [soc.key()]
		model = Crisis()
		model.socials = soclist
		self.assertTrue(db.get(model.socials[0]).site == "Facebook")
		self.assertTrue(db.get(model.socials[0]).title == "Chile Earthquake")
		self.assertTrue(db.get(model.socials[0]).url == "https://www.facebook.com/chileearthquakeupdate?filter=3")
		self.assertTrue(db.get(model.socials[0]).description == "Coverage of the events of the Chilean Earthquake as they unfolded.")


	def test_Crisis_externals(self):
		ext = Media(site = "State", title = "US Department of State", url = "http://www.state.gov/p/wha/ci/ci/earthquake/index.htm", description = "US gov website on Chile earthquake")
		ext.put()
		extlist = [ext.key()]
		model = Crisis()
		model.externals = extlist
		self.assertTrue(db.get(model.externals[0]).site == "State")
		self.assertTrue(db.get(model.externals[0]).title == "US Department of State")
		self.assertTrue(db.get(model.externals[0]).url == "http://www.state.gov/p/wha/ci/ci/earthquake/index.htm")
		self.assertTrue(db.get(model.externals[0]).description == "US gov website on Chile earthquake")


	def test_Organization_attr(self):
		model = Organization(identifier = "SalvationArmy", name = "Salvation Army", info_type = "Educational", misc = "The Outreach Programme on the Rwanda Genocide and the United Nations is an information and educational outreach programme run by the United Nations Department of Public Information.", location_city = "Alexandria", location_region = "North America", location_country = "USA", history = "The Salvation Army was founded in London's East End in 1865 with a quasi-military structure by one-time Methodist minister William Booth and his wife Catherine.", contact_phone = "232-323-2222", contact_email = "admin@salv.com", contact_mail_address = "316 Fall Creek Dr.", contact_mail_city = "Dallas", contact_mail_state = "Texas", contact_mail_country = "Argentina", contact_mail_zip  = "75080")
		self.assertTrue(model.identifier == "SalvationArmy")
		self.assertTrue(model.name == "Salvation Army")
		self.assertTrue(model.info_type == "Educational")
		self.assertTrue(model.misc == "The Outreach Programme on the Rwanda Genocide and the United Nations is an information and educational outreach programme run by the United Nations Department of Public Information.")
		self.assertTrue(model.location_city == "Alexandria")
		self.assertTrue(model.location_region == "North America")
		self.assertTrue(model.location_country == "USA")
		self.assertTrue(model.history == "The Salvation Army was founded in London's East End in 1865 with a quasi-military structure by one-time Methodist minister William Booth and his wife Catherine.")
		self.assertTrue(model.contact_phone == "232-323-2222")
		self.assertTrue(model.contact_email == "admin@salv.com")
		self.assertTrue(model.contact_mail_address == "316 Fall Creek Dr.")
		self.assertTrue(model.contact_mail_city == "Dallas")
		self.assertTrue(model.contact_mail_state == "Texas")
		self.assertTrue(model.contact_mail_country == "Argentina")
		self.assertTrue(model.contact_mail_zip  == "75080")

	def test_Organization_primaryImage(self):
		img = Media(site = "Wikipedia", title = "Salvation Army Crest", url = "http://upload.wikimedia.org/wikipedia/en/f/fd/Crest_of_The_Salvation_Army.png", description = "The oldest official emblem of the salvation army")
		model = Organization()
		model.primaryImage = img
		self.assertTrue(model.primaryImage.site == "Wikipedia")
		self.assertTrue(model.primaryImage.title == "Salvation Army Crest")
		self.assertTrue(model.primaryImage.url =="http://upload.wikimedia.org/wikipedia/en/f/fd/Crest_of_The_Salvation_Army.png")
		self.assertTrue(model.primaryImage.description == "The oldest official emblem of the salvation army")


	def test_Organization_images(self):
		img = Media(site = "Wikipedia", title = "The Salvation Army", url = "http://upload.wikimedia.org/wikipedia/en/c/c4/The_Salvation_Army.svg", description = "The Salvation Army's logo")
		img.put()
		imglist = [img.key()]
		model = Organization()
		model.images = imglist
		self.assertTrue(db.get(model.images[0]).site == "Wikipedia")
		self.assertTrue(db.get(model.images[0]).title == "The Salvation Army")
		self.assertTrue(db.get(model.images[0]).url == "http://upload.wikimedia.org/wikipedia/en/c/c4/The_Salvation_Army.svg")
		self.assertTrue(db.get(model.images[0]).description == "The Salvation Army's logo")

	def test_Organization_videos(self):
		vid = Media(site = "YouTube", title = "Salvation Army 2008 Annual Report", url = "http://www.youtube.com/embed/VjxQCMNqflw", description = "A collection of the Salvation Army's major accomplishments and events in 2008.")
		vid.put()
		vidlist = [vid.key()]
		model = Organization()
		model.videos = vidlist
		self.assertTrue(db.get(model.videos[0]).site == "YouTube")
		self.assertTrue(db.get(model.videos[0]).title == "Salvation Army 2008 Annual Report")
		self.assertTrue(db.get(model.videos[0]).url == "http://www.youtube.com/embed/VjxQCMNqflw")
		self.assertTrue(db.get(model.videos[0]).description == "A collection of the Salvation Army's major accomplishments and events in 2008.")

	def test_Organization_socials(self):
		soc = Media(site = "Facebook", title = "The Salvation Army USA Branch", url = "https://www.facebook.com/SalvationArmyUSA", description = "The facebook page of the Salvation Army's USA branch.")
		soc.put()
		soclist = [soc.key()]
		model = Organization()
		model.socials = soclist
		self.assertTrue(db.get(model.socials[0]).site == "Facebook")
		self.assertTrue(db.get(model.socials[0]).title == "The Salvation Army USA Branch")
		self.assertTrue(db.get(model.socials[0]).url == "https://www.facebook.com/SalvationArmyUSA")
		self.assertTrue(db.get(model.socials[0]).description == "The facebook page of the Salvation Army's USA branch.")


	def test_Organization_externals(self):
		ext = Media(site = "Salvation Army", title = "Salvation Army", url = "http://www.salvationarmyusa.org", description = "Official Salvation Army Website")
		ext.put()
		extlist = [ext.key()]
		model = Organization()
		model.externals = extlist
		self.assertTrue(db.get(model.externals[0]).site == "Salvation Army")
		self.assertTrue(db.get(model.externals[0]).title == "Salvation Army")
		self.assertTrue(db.get(model.externals[0]).url == "http://www.salvationarmyusa.org")
		self.assertTrue(db.get(model.externals[0]).description == "Official Salvation Army Website")


	def test_Person_attr(self):
		model = Person(identifier = "PaulRuse", name = "Paul Ruse", info_type = "Natural Disaster", misc = "Paul Rusesabagina is a Rwandan humanitarian known for hiding and protecting 1,268 refugees during the Rwandan Genocide.", birthdate_time = "9:15", birthdate_day  = 25, birthdate_month = 06, birthdate_year = 1906, birthdate_misc = "born in a leap year", nationality = "American", biography = "Michael Johanns is an American Republican politician.")
		self.assertTrue(model.identifier == "PaulRuse")
		self.assertTrue(model.name == "Paul Ruse")
		self.assertTrue(model.info_type == "Natural Disaster")
		self.assertTrue(model.misc == "Paul Rusesabagina is a Rwandan humanitarian known for hiding and protecting 1,268 refugees during the Rwandan Genocide.")
		self.assertTrue(model.birthdate_time == "9:15")
		self.assertTrue(model.birthdate_day  == 25)
		self.assertTrue(model.birthdate_month == 06)
		self.assertTrue(model.birthdate_year == 1906)
		self.assertTrue(model.birthdate_misc == "born in a leap year")
		self.assertTrue(model.nationality == "American")
		self.assertTrue(model.biography == "Michael Johanns is an American Republican politician.")

	def test_Person_primaryImage(self):
		img = Media(site = "Wikipedia", title = "Michelle Bachelet", url = "http://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Michele_Bachelet_(2009).jpg/220px-Michele_Bachelet_(2009).jpg", description = "Michelle greeting followers at a gathering.")
		model = Person()
		model.primaryImage = img
		self.assertTrue(model.primaryImage.site == "Wikipedia")
		self.assertTrue(model.primaryImage.title == "Michelle Bachelet")
		self.assertTrue(model.primaryImage.url =="http://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Michele_Bachelet_(2009).jpg/220px-Michele_Bachelet_(2009).jpg")
		self.assertTrue(model.primaryImage.description == "Michelle greeting followers at a gathering.")


	def test_Person_images(self):
		img = Media(site = "Zimbio", title = "Michelle Bachelet with President Obama", url = "http://www1.pictures.zimbio.com/gi/Obama+Meets+President+Chile+Michelle+Bachelet+wqqyp-anShzl.jpg", description = "Obama Meets With President Of Chile Michelle Bachelet")
		img.put()
		imglist = [img.key()]
		model = Person()
		model.images = imglist
		self.assertTrue(db.get(model.images[0]).site == "Zimbio")
		self.assertTrue(db.get(model.images[0]).title == "Michelle Bachelet with President Obama")
		self.assertTrue(db.get(model.images[0]).url == "http://www1.pictures.zimbio.com/gi/Obama+Meets+President+Chile+Michelle+Bachelet+wqqyp-anShzl.jpg")
		self.assertTrue(db.get(model.images[0]).description == "Obama Meets With President Of Chile Michelle Bachelet")

	def test_Person_videos(self):
		vid = Media(site = "YouTube", title = "Tea with Michelle Bachelet on UN Women", url = "http://www.youtube.com/embed/X2toGWWuUkk", description = "Former President of Chile Michelle Bachelet talks about serving as the director of UN Women.")
		vid.put()
		vidlist = [vid.key()]
		model = Person()
		model.videos = vidlist
		self.assertTrue(db.get(model.videos[0]).site == "YouTube")
		self.assertTrue(db.get(model.videos[0]).title == "Tea with Michelle Bachelet on UN Women")
		self.assertTrue(db.get(model.videos[0]).url == "http://www.youtube.com/embed/X2toGWWuUkk")
		self.assertTrue(db.get(model.videos[0]).description == "Former President of Chile Michelle Bachelet talks about serving as the director of UN Women.")

	def test_Person_socials(self):
		soc = Media(site = "Facebook", title = "Michelle Bachelet Fan Page", url = "https://www.facebook.com/pages/Michelle-Bachelet/8459707345", description = "A facebook fan page of Michelle Bachelet")
		soc.put()
		soclist = [soc.key()]
		model = Person()
		model.socials = soclist
		self.assertTrue(db.get(model.socials[0]).site == "Facebook")
		self.assertTrue(db.get(model.socials[0]).title == "Michelle Bachelet Fan Page")
		self.assertTrue(db.get(model.socials[0]).url == "https://www.facebook.com/pages/Michelle-Bachelet/8459707345")
		self.assertTrue(db.get(model.socials[0]).description == "A facebook fan page of Michelle Bachelet")

	def test_Person_externals(self):
		ext = Media(site = "Britannica", title = "Britannica", url = "http://www.britannica.com/EBchecked/topic/1009973/Michelle-Bachelet", description = "Info on Michelle Bachelet")
		ext.put()
		extlist = [ext.key()]
		model = Person()
		model.externals = extlist
		self.assertTrue(db.get(model.externals[0]).site == "Britannica")
		self.assertTrue(db.get(model.externals[0]).title == "Britannica")
		self.assertTrue(db.get(model.externals[0]).url == "http://www.britannica.com/EBchecked/topic/1009973/Michelle-Bachelet")
		self.assertTrue(db.get(model.externals[0]).description == "Info on Michelle Bachelet")

  

def test_main():
	test_support.run_unittest(MyTestCase1)

if __name__ == '__main__':
    test_main()
