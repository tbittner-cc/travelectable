PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE us_metro_areas (
	id INTEGER NOT NULL, 
	metro_area VARCHAR, 
	population VARCHAR, 
	city VARCHAR, 
	state VARCHAR, 
	country VARCHAR, 
	latitude VARCHAR, 
	longitude VARCHAR, 
	description VARCHAR, 
	points_of_interest VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO us_metro_areas VALUES(1,'New York-Newark-Jersey City, NY-NJ-PA','19,620,000','New York','NY','USA','40.7128','-74.0060',NULL,NULL);
INSERT INTO us_metro_areas VALUES(2,'Los Angeles-Long Beach-Anaheim, CA','12,770,000','Los Angeles','CA','USA','34.0522','-118.2437',NULL,NULL);
INSERT INTO us_metro_areas VALUES(3,'Chicago-Naperville-Elgin, IL-IN-WI','9,110,000','Chicago','IL','USA','41.8781','-87.6298',NULL,NULL);
INSERT INTO us_metro_areas VALUES(4,'Houston-The Woodlands-Sugar Land, TX','6,770,000','Houston','TX','USA','29.7633','-95.3632',NULL,NULL);
INSERT INTO us_metro_areas VALUES(5,'Phoenix-Mesa-Scottsdale, AZ','4,920,000','Phoenix','AZ','USA','33.4484','-112.0739',NULL,NULL);
INSERT INTO us_metro_areas VALUES(6,'Philadelphia-Camden-Wilmington, PA-NJ-DE-MD','6,240,000','Philadelphia','PA','USA','39.9523','-75.1631',NULL,NULL);
INSERT INTO us_metro_areas VALUES(7,'San Antonio-New Braunfels, TX','2,530,000','San Antonio','TX','USA','29.4241','-98.4936',NULL,NULL);
INSERT INTO us_metro_areas VALUES(8,'San Diego-Carlsbad, CA','3,330,000','San Diego','CA','USA','32.7157','-117.1611',NULL,NULL);
INSERT INTO us_metro_areas VALUES(9,'Dallas-Fort Worth-Arlington, TX','7,520,000','Dallas','TX','USA','32.7767','-96.7969',NULL,NULL);
INSERT INTO us_metro_areas VALUES(10,'San Jose-Sunnyvale-Santa Clara, CA','3,270,000','San Jose','CA','USA','37.3382','-121.8863',NULL,NULL);
INSERT INTO us_metro_areas VALUES(11,'Austin-Round Rock-Georgetown, TX','2,170,000','Austin','TX','USA','30.2671','-97.7437',NULL,NULL);
INSERT INTO us_metro_areas VALUES(12,'Jacksonville, FL','1,540,000','Jacksonville','FL','USA','30.3321','-81.6557',NULL,NULL);
INSERT INTO us_metro_areas VALUES(13,'San Francisco-Oakland-Hayward, CA','3,310,000','San Francisco','CA','USA','37.7749','-122.4194',NULL,NULL);
INSERT INTO us_metro_areas VALUES(14,'Indianapolis-Carmel-Anderson, IN','2,050,000','Indianapolis','IN','USA','39.7684','-86.1580',NULL,NULL);
INSERT INTO us_metro_areas VALUES(15,'Columbus, OH','2,130,000','Columbus','OH','USA','39.9611','-82.9988',NULL,NULL);
INSERT INTO us_metro_areas VALUES(16,'Fort Worth-Arlington, TX','2,900,000','Fort Worth','TX','USA','32.7555','-97.3308',NULL,NULL);
INSERT INTO us_metro_areas VALUES(17,'Charlotte-Concord-Gastonia, NC-SC','2,660,000','Charlotte','NC','USA','35.2240','-80.8431',NULL,NULL);
INSERT INTO us_metro_areas VALUES(18,'Memphis, TN-MS-AR','1,340,000','Memphis','TN','USA','35.1495','-90.0488',NULL,NULL);
INSERT INTO us_metro_areas VALUES(19,'Boston-Cambridge-Nashua, MA-NH','4,900,000','Boston','MA','USA','42.3601','-71.0589',NULL,NULL);
INSERT INTO us_metro_areas VALUES(20,'Baltimore-Columbia-Towson, MD','2,840,000','Baltimore','MD','USA','39.2905','-76.6122',NULL,NULL);
INSERT INTO us_metro_areas VALUES(21,'Detroit-Warren-Dearborn, MI','4,320,000','Detroit','MI','USA','42.3314','-83.0458',NULL,NULL);
INSERT INTO us_metro_areas VALUES(22,'El Paso, TX','844,000','El Paso','TX','USA','31.7587','-106.4623',NULL,NULL);
INSERT INTO us_metro_areas VALUES(23,'Seattle-Tacoma-Bellevue, WA','4,030,000','Seattle','WA','USA','47.6062','-122.3321',NULL,NULL);
INSERT INTO us_metro_areas VALUES(24,'Denver-Aurora-Lakewood, CO','3,030,000','Denver','CO','USA','39.7392','-104.9903',NULL,NULL);
INSERT INTO us_metro_areas VALUES(25,'Milwaukee-Waukesha-West Allis, WI','1,570,000','Milwaukee','WI','USA','43.0389','-87.9065',NULL,NULL);
INSERT INTO us_metro_areas VALUES(26,'Portland-Vancouver-Hillsboro, OR-WA','2,510,000','Portland','OR','USA','45.5231','-122.6750',NULL,NULL);
INSERT INTO us_metro_areas VALUES(27,'Oklahoma City, OK','1,390,000','Oklahoma City','OK','USA','35.4676','-97.5164',NULL,NULL);
INSERT INTO us_metro_areas VALUES(28,'Nashville-Davidson--Murfreesboro--Franklin, TN','1,930,000','Nashville','TN','USA','36.1627','-86.7816',NULL,NULL);
INSERT INTO us_metro_areas VALUES(29,'Washington-Arlington-Alexandria, DC-VA-MD','6,280,000','Washington DC','','USA','38.8951','-77.0367',NULL,NULL);
INSERT INTO us_metro_areas VALUES(30,'Kansas City, MO-KS','2,190,000','Kansas City','MO','USA','39.0997','-94.5786',NULL,NULL);
INSERT INTO us_metro_areas VALUES(31,'St. Louis, MO-IL','2,820,000','St. Louis','MO','USA','38.6270','-90.1994',NULL,NULL);
INSERT INTO us_metro_areas VALUES(32,'Raleigh, NC','1,440,000','Raleigh','NC','USA','35.7796','-78.6382',NULL,NULL);
INSERT INTO us_metro_areas VALUES(33,'Cleveland-Elyria, OH','2,150,000','Cleveland','OH','USA','41.4995','-81.6954',NULL,NULL);
INSERT INTO us_metro_areas VALUES(34,'Miami-Fort Lauderdale-Pompano Beach, FL','6,110,000','Miami','FL','USA','25.7617','-80.1918',NULL,NULL);
INSERT INTO us_metro_areas VALUES(35,'Oakland-Hayward-Berkeley, CA','2,700,000','Oakland','CA','USA','37.8044','-122.2711',NULL,NULL);
INSERT INTO us_metro_areas VALUES(36,'Minneapolis-St. Paul-Bloomington, MN-WI','3,930,000','Minneapolis','MN','USA','44.9778','-93.2643',NULL,NULL);
INSERT INTO us_metro_areas VALUES(37,'Tulsa, OK','984,000','Tulsa','OK','USA','36.1530','-95.9928',NULL,NULL);
INSERT INTO us_metro_areas VALUES(38,'Virginia Beach-Norfolk-Newport News, VA-NC','1,740,000','Virginia Beach','VA','USA','36.8507','-76.0749',NULL,NULL);
INSERT INTO us_metro_areas VALUES(39,'Sacramento-Roseville-Arden-Arcade, CA','2,590,000','Sacramento','CA','USA','38.5816','-121.4944',NULL,NULL);
INSERT INTO us_metro_areas VALUES(40,'Las Vegas-Henderson-Paradise, NV','2,820,000','Las Vegas','NV','USA','36.1697','-115.1398',NULL,NULL);
INSERT INTO us_metro_areas VALUES(41,'Louisville/Jefferson County, KY-IN','1,270,000','Louisville','KY','USA','38.2542','-85.7603',NULL,NULL);
INSERT INTO us_metro_areas VALUES(42,'San Francisco-San Mateo-Redwood City, CA','2,550,000','San Francisco','CA','USA','37.7749','-122.4194',NULL,NULL);
INSERT INTO us_metro_areas VALUES(43,'New Orleans-Metairie, LA','1,260,000','New Orleans','LA','USA','29.9511','-90.0715',NULL,NULL);
INSERT INTO us_metro_areas VALUES(44,'Cincinnati, OH-KY-IN','2,130,000','Cincinnati','OH','USA','39.1031','-84.5120',NULL,NULL);
INSERT INTO us_metro_areas VALUES(45,'Pittsburgh, PA','2,330,000','Pittsburgh','PA','USA','40.4406','-79.9969',NULL,NULL);
INSERT INTO us_metro_areas VALUES(46,'Orlando-Kissimmee-Sanford, FL','2,570,000','Orlando','FL','USA','28.5384','-81.3792',NULL,NULL);
INSERT INTO us_metro_areas VALUES(47,'St. Paul-Minneapolis-Bloomington, MN-WI','3,930,000','Minneapolis','MN','USA','44.9778','-93.2650',NULL,NULL);
INSERT INTO us_metro_areas VALUES(48,'Greenville-Anderson-Mauldin, SC','920,000','Greenville','SC','USA','34.8526','-82.3940',NULL,NULL);
INSERT INTO us_metro_areas VALUES(49,'Cleveland-Lorain-Elyria, OH','2,150,000','Cleveland','OH','USA','41.4993','-81.6954',NULL,NULL);
INSERT INTO us_metro_areas VALUES(50,'Tampa-St. Petersburg-Clearwater, FL','4,310,000','Tampa','FL','USA','27.9475','-82.4584',NULL,NULL);
INSERT INTO us_metro_areas VALUES(51,'Anchorage, AK','398,000','Anchorage','AK','USA','66.1605','-153.3691',NULL,NULL);
INSERT INTO us_metro_areas VALUES(52,'Honolulu, HI','920,000','Honolulu','HI','USA','21.3156','-157.8580',NULL,NULL);
INSERT INTO us_metro_areas VALUES(53,'San Juan, PR','2,443,000','San Juan','PR','USA','18.4663','-66.1057',NULL,NULL);
CREATE TABLE us_destinations (
	id INTEGER NOT NULL, 
	location VARCHAR, 
	state VARCHAR, 
	latitude VARCHAR, 
	longitude VARCHAR, 
	nearest_metro_area VARCHAR, 
	country VARCHAR, 
	description VARCHAR, 
	points_of_interest VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO us_destinations VALUES(1,'Acadia National Park','ME','44.35','-68.21','Boston-Cambridge-Nashua, MA-NH','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(2,'Asheville','NC','35.59','-82.55','Greenville-Anderson-Mauldin, SC','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(3,'Bar Harbor','ME','44.39','-68.20','Boston-Cambridge-Nashua, MA-NH','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(4,'Bend','OR','44.06','-121.31','Portland-Vancouver-Hillsboro, OR-WA','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(5,'Big Sur','CA','36.22','-121.67','San Jose-Sunnyvale-Santa Clara, CA','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(6,'Branson','MO','36.6439','-93.2183','Tulsa, OK','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(7,'Breckenridge','CO','39.4822','-106.0382','Denver-Aurora-Lakewood, CO','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(8,'Cape Cod','MA','41.9333','-70.0167','Boston-Cambridge-Nashua, MA-NH','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(9,'Charleston','SC','32.7857','-79.9339','Charlotte-Concord-Gastonia, NC-SC','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(10,'Cooperstown','NY','42.6978','-74.9239','New York-Newark-Jersey City, NY-NJ-PA','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(11,'Custer State Park','SD','43.75','-103.43','Denver-Aurora-Lakewood, CO','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(12,'Durango','CO','37.28','-107.88','Denver-Aurora-Lakewood, CO','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(13,'Gatlinburg','TN','35.71','-83.52','Greenville-Anderson-Mauldin, SC','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(14,'Glacier National Park','MT','48.77','-113.67','Seattle-Tacoma-Bellevue, WA','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(15,'Glenwood Springs','CO','39.55','-107.32','Denver-Aurora-Lakewood, CO','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(16,'Grand Canyon','AZ','36.0544','-112.1401','Las Vegas-Henderson-Paradise, NV','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(17,'Great Smoky Mountains National Park','TN','35.6184','-83.5302','Greenville-Anderson-Mauldin, SC','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(18,'Jackson Hole','WY','43.5825','-110.8219','Denver-Aurora-Lakewood, CO','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(19,'Kauai','HI','22.0827','-159.4983','Honolulu, HI','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(20,'Key West','FL','24.5551','-81.7801','Miami-Fort Lauderdale-Pompano Beach, FL','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(21,'Lake Tahoe','CA','39.0942','-120.0424','Sacramento-Roseville-Arden-Arcade, CA','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(22,'Mackinac Island','MI','45.8497','-84.6278','Milwaukee-Waukesha-West Allis, WI','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(23,'Maui','HI','20.7984','-156.3314','Honolulu, HI','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(24,'Mount Rushmore','SD','43.8794','-103.4597','Denver-Aurora-Lakewood, CO','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(25,'Myrtle Beach','SC','33.6926','-78.8867','Raleigh, NC','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(26,'Napa Valley','CA','38.2977','-122.2864','Oakland-Hayward-Berkeley, CA','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(27,'Olympic National Park','WA','47.5714','-123.4431','Seattle-Tacoma-Bellevue, WA','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(28,'Palm Springs','CA','33.8303','-116.5453','San Diego-Carlsbad, CA','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(29,'Santa Fe','NM','35.6869','-105.9378','El Paso, TX','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(30,'Savannah','GA','32.0835','-81.0998','Jacksonville, FL','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(31,'Sedona','AZ','34.8697','-111.7603','Phoenix-Mesa-Scottsdale, AZ','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(32,'St. Augustine','FL','29.8942','-81.3145','Jacksonville, FL','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(33,'Telluride','CO','37.9375','-107.8206','Denver-Aurora-Lakewood, CO','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(34,'Williamsburg','VA','37.2707','-76.7074','Virginia Beach-Norfolk-Newport News, VA-NC','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(35,'Yellowstone National Park','WY','44.4275','-110.5885','Denver-Aurora-Lakewood, CO','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(36,'Yosemite National Park','CA','37.7447','-119.5882','Sacramento-Roseville-Arden-Arcade, CA','USA',NULL,NULL);
INSERT INTO us_destinations VALUES(37,'Zion National Park','UT','37.2986','-113.0267','Las Vegas-Henderson-Paradise, NV','USA',NULL,NULL);
CREATE TABLE intl_destinations (
	id INTEGER NOT NULL, 
	location VARCHAR, 
	country VARCHAR, 
	latitude VARCHAR, 
	longitude VARCHAR, 
	travel_advisory_level VARCHAR(30), 
	description VARCHAR, 
	points_of_interest VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO intl_destinations VALUES(1,'Amsterdam','Netherlands','52.3702','4.8903','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(2,'Aruba Island','Aruba','12.5079','-70.0353','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(3,'Athens','Greece','37.9838','23.7275','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(4,'Auckland','New Zealand','-36.8485','174.7633','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(5,'Bali','Indonesia','-8.4095','115.1889','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(6,'Bangkok','Thailand','13.7563','100.5018','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(7,'Barcelona','Spain','41.3851','2.1734','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(8,'Beijing','China','39.9042','116.3974','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(9,'Berlin','Germany','52.5200','13.4050','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(10,'Bogota','Colombia','4.6097','-74.0817','Reconsider Travel',NULL,NULL);
INSERT INTO intl_destinations VALUES(11,'Buenos Aires','Argentina','-34.6037','-58.3816','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(12,'Cabo San Lucas','Mexico','22.8869','-109.4253','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(13,'Cairo','Egypt','30.0522','31.2497','Reconsider Travel',NULL,NULL);
INSERT INTO intl_destinations VALUES(14,'Cancun','Mexico','21.1743','-86.8466','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(15,'Cape Town','South Africa','-33.9249','18.4241','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(16,'Casablanca','Morocco','33.5928','-7.9222','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(17,'Copenhagen','Denmark','55.6763','12.5681','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(18,'Delhi','India','28.6139','77.2090','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(19,'Dubai','United Arab Emirates','25.0657','55.1713','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(20,'Dublin','Ireland','53.3441','-6.2672','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(21,'Dubrovnik','Croatia','42.6481','18.0921','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(22,'Edinburgh','Scotland','55.9533','-3.1883','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(23,'George Town','Cayman Islands','19.2937','-81.3865','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(24,'Hanoi','Vietnam','21.0278','105.8342','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(25,'Helsinki','Finland','60.1699','24.9384','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(26,'Ho Chi Minh City','Vietnam','10.7626','106.6747','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(27,'Hong Kong','China','22.3964','114.1095','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(28,'Istanbul','Turkey','41.0082','28.9744','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(29,'Jerusalem','Israel','31.7833','35.2167','Reconsider Travel',NULL,NULL);
INSERT INTO intl_destinations VALUES(30,'Kuala Lumpur','Malaysia','3.1390','101.6869','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(31,'Lima','Peru','-12.0464','-77.0428','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(32,'Lisbon','Portugal','38.7223','-9.1393','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(33,'London','England','51.5074','-0.1278','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(34,'Macau','China','22.1667','113.5500','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(35,'Madrid','Spain','40.4168','-3.7033','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(36,'Manila','Philippines','14.5995','121.0817','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(37,'Marrakech','Morocco','31.6295','-7.9811','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(38,'Mexico City','Mexico','19.4326','-99.1332','Reconsider Travel',NULL,NULL);
INSERT INTO intl_destinations VALUES(39,'Montego Bay','Jamaica','18.5093','-77.8947','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(40,'Montreal','Canada','45.5017','-73.5673','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(41,'Moscow','Russia','55.7558','37.6173','Do Not Travel',NULL,NULL);
INSERT INTO intl_destinations VALUES(42,'Mumbai','India','19.0759','72.8777','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(43,'Nassau','Bahamas','25.0582','-77.3434','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(44,'Oslo','Norway','59.9139','10.7522','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(45,'Panama City','Panama','9.0007','-79.5163','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(46,'Paris','France','48.8567','2.3522','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(47,'Phuket','Thailand','7.8906','98.3923','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(48,'Prague','Czech Republic','50.0755','14.4378','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(49,'Puerto Vallarta','Mexico','20.6773','-105.2447','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(50,'Punta Cana','Dominican Republic','18.5667','-68.4167','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(51,'Reykjavik','Iceland','64.1353','-21.8954','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(52,'Rio de Janeiro','Brazil','-22.9068','-43.1729','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(53,'Rome','Italy','41.8719','12.4964','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(54,'San Jose','Costa Rica','9.9281','-84.0907','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(55,'San Salvador','El Salvador','13.6892','-89.2012','Reconsider Travel',NULL,NULL);
INSERT INTO intl_destinations VALUES(56,'Santiago','Chile','-33.4378','-70.6506','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(57,'Santorini','Greece','36.3932','25.4597','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(58,'Seoul','South Korea','37.5665','126.9778','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(59,'Shanghai','China','31.2304','121.4737','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(60,'Singapore','Singapore','1.3521','103.8198','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(61,'Split','Croatia','43.5065','16.4439','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(62,'St. Petersburg','Russia','59.9389','30.3256','Do Not Travel',NULL,NULL);
INSERT INTO intl_destinations VALUES(63,'Stockholm','Sweden','59.3293','18.0686','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(64,'Sydney','Australia','-33.8651','151.2099','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(65,'Taipei','Taiwan','25.0478','121.5319','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(66,'Tel Aviv','Israel','32.0853','34.7804','Exercise Increased Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(67,'Tokyo','Japan','35.6895','139.7670','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(68,'Toronto','Canada','43.6532','-79.3832','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(69,'Vancouver','Canada','49.2827','-123.1207','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(70,'Vienna','Austria','48.2082','16.3738','Exercise Normal Precautions',NULL,NULL);
INSERT INTO intl_destinations VALUES(71,'Zurich','Switzerland','47.3769','8.5382','Exercise Normal Precautions',NULL,NULL);
COMMIT;
