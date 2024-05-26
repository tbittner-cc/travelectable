PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE destinations (
        id INTEGER PRIMARY KEY autoincrement,
        location VARCHAR,
        city VARCHAR,
        state VARCHAR,
        country VARCHAR,
        latitude VARCHAR,
        longitude VARCHAR,
        description VARCHAR,
        points_of_interest VARCHAR,
        nearest_metro_area VARCHAR,
        travel_advisory_level VARCHAR(30)
    , hotel_retries int default 0);
INSERT INTO destinations VALUES(1,'New York-Newark-Jersey City, NY-NJ-PA','New York','NY','USA','40.7128','-74.0060','Experience the city that never sleeps! New York, NY is a world-class destination that offers something for everyone. From iconic landmarks like the Statue of Liberty and Central Park to world-renowned museums like the Met and MoMA, the city is steeped in history and culture. Take in the bright lights and bustling energy of Times Square, catch a Broadway show, or explore the trendy neighborhoods of SoHo and Greenwich Village. With unparalleled dining, shopping, and entertainment options, New York City is the ultimate urban adventure. Come and discover why it''s the city that has it all!','[''Statue of Liberty'', ''Central Park'', ''The Metropolitan Museum of Art'', ''Empire State Building'', ''Times Square'']',NULL,NULL,0);
INSERT INTO destinations VALUES(2,'Los Angeles-Long Beach-Anaheim, CA','Los Angeles','CA','USA','34.0522','-118.2437','Experience the ultimate urban getaway in Los Angeles, where sun-kissed beaches meet vibrant city streets. Discover iconic landmarks like the Hollywood Sign, Griffith Observatory, and Universal Studios Hollywood. Indulge in world-class dining, shopping, and nightlife in trendy neighborhoods like Santa Monica, Venice, and Silverlake. Get your dose of art and culture at the Getty Center, LACMA, and Walt Disney Concert Hall. And, of course, soak up the laid-back California vibe on Malibu beaches or hike to breathtaking views in Runyon Canyon. LA has something for everyone – come and create your own unforgettable adventure!','[''Universal Studios Hollywood'', '' Griffith Observatory'', '' Getty Center'', '' Santa Monica Pier'', '' Walk of Fame'']',NULL,NULL,0);
INSERT INTO destinations VALUES(3,'Chicago-Naperville-Elgin, IL-IN-WI','Chicago','IL','USA','41.8781','-87.6298','Experience the vibrant energy of Chicago, where stunning architecture meets world-class culture and entertainment. Stroll along Lake Michigan''s shores, take in the breathtaking views of the city skyline, and explore iconic landmarks like Willis Tower and Navy Pier. Discover world-renowned museums like the Art Institute of Chicago and Field Museum, and indulge in the city''s famous deep-dish pizza and craft beer scene. From Wrigley Field to Millennium Park, Chicago''s neighborhoods are bursting with character and charm. Come for the attractions, stay for the Midwestern hospitality – Chicago is the ultimate urban getaway.','[''Willis Tower (formerly Sears Tower)'', ''Millennium Park'', ''Navy Pier'', ''The Art Institute of Chicago'', ''Wrigley Field'']',NULL,NULL,0);
INSERT INTO destinations VALUES(4,'Houston-The Woodlands-Sugar Land, TX','Houston','TX','USA','29.7633','-95.3632',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(5,'Phoenix-Mesa-Scottsdale, AZ','Phoenix','AZ','USA','33.4484','-112.0739',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(6,'Philadelphia-Camden-Wilmington, PA-NJ-DE-MD','Philadelphia','PA','USA','39.9523','-75.1631',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(7,'San Antonio-New Braunfels, TX','San Antonio','TX','USA','29.4241','-98.4936',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(8,'San Diego-Carlsbad, CA','San Diego','CA','USA','32.7157','-117.1611',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(9,'Dallas-Fort Worth-Arlington, TX','Dallas','TX','USA','32.7767','-96.7969',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(10,'San Jose-Sunnyvale-Santa Clara, CA','San Jose','CA','USA','37.3382','-121.8863',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(11,'Austin-Round Rock-Georgetown, TX','Austin','TX','USA','30.2671','-97.7437',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(12,'Jacksonville, FL','Jacksonville','FL','USA','30.3321','-81.6557',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(13,'San Francisco-Oakland-Hayward, CA','San Francisco','CA','USA','37.7749','-122.4194',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(14,'Indianapolis-Carmel-Anderson, IN','Indianapolis','IN','USA','39.7684','-86.1580',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(15,'Columbus, OH','Columbus','OH','USA','39.9611','-82.9988',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(16,'Fort Worth-Arlington, TX','Fort Worth','TX','USA','32.7555','-97.3308',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(17,'Charlotte-Concord-Gastonia, NC-SC','Charlotte','NC','USA','35.2240','-80.8431',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(18,'Memphis, TN-MS-AR','Memphis','TN','USA','35.1495','-90.0488',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(19,'Boston-Cambridge-Nashua, MA-NH','Boston','MA','USA','42.3601','-71.0589',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(20,'Baltimore-Columbia-Towson, MD','Baltimore','MD','USA','39.2905','-76.6122',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(21,'Detroit-Warren-Dearborn, MI','Detroit','MI','USA','42.3314','-83.0458',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(22,'El Paso, TX','El Paso','TX','USA','31.7587','-106.4623',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(23,'Seattle-Tacoma-Bellevue, WA','Seattle','WA','USA','47.6062','-122.3321',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(24,'Denver-Aurora-Lakewood, CO','Denver','CO','USA','39.7392','-104.9903',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(25,'Milwaukee-Waukesha-West Allis, WI','Milwaukee','WI','USA','43.0389','-87.9065',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(26,'Portland-Vancouver-Hillsboro, OR-WA','Portland','OR','USA','45.5231','-122.6750',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(27,'Oklahoma City, OK','Oklahoma City','OK','USA','35.4676','-97.5164',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(28,'Nashville-Davidson--Murfreesboro--Franklin, TN','Nashville','TN','USA','36.1627','-86.7816',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(29,'Washington-Arlington-Alexandria, DC-VA-MD','Washington DC','','USA','38.8951','-77.0367',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(30,'Kansas City, MO-KS','Kansas City','MO','USA','39.0997','-94.5786',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(31,'St. Louis, MO-IL','St. Louis','MO','USA','38.6270','-90.1994',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(32,'Raleigh, NC','Raleigh','NC','USA','35.7796','-78.6382',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(33,'Cleveland-Elyria, OH','Cleveland','OH','USA','41.4995','-81.6954',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(34,'Miami-Fort Lauderdale-Pompano Beach, FL','Miami','FL','USA','25.7617','-80.1918',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(35,'Oakland-Hayward-Berkeley, CA','Oakland','CA','USA','37.8044','-122.2711',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(36,'Minneapolis-St. Paul-Bloomington, MN-WI','Minneapolis','MN','USA','44.9778','-93.2643',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(37,'Tulsa, OK','Tulsa','OK','USA','36.1530','-95.9928',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(38,'Virginia Beach-Norfolk-Newport News, VA-NC','Virginia Beach','VA','USA','36.8507','-76.0749',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(39,'Sacramento-Roseville-Arden-Arcade, CA','Sacramento','CA','USA','38.5816','-121.4944',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(40,'Las Vegas-Henderson-Paradise, NV','Las Vegas','NV','USA','36.1697','-115.1398',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(41,'Louisville/Jefferson County, KY-IN','Louisville','KY','USA','38.2542','-85.7603',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(42,'San Francisco-San Mateo-Redwood City, CA','San Francisco','CA','USA','37.7749','-122.4194',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(43,'New Orleans-Metairie, LA','New Orleans','LA','USA','29.9511','-90.0715',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(44,'Cincinnati, OH-KY-IN','Cincinnati','OH','USA','39.1031','-84.5120',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(45,'Pittsburgh, PA','Pittsburgh','PA','USA','40.4406','-79.9969',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(46,'Orlando-Kissimmee-Sanford, FL','Orlando','FL','USA','28.5384','-81.3792',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(47,'St. Paul-Minneapolis-Bloomington, MN-WI','Minneapolis','MN','USA','44.9778','-93.2650',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(48,'Greenville-Anderson-Mauldin, SC','Greenville','SC','USA','34.8526','-82.3940',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(49,'Cleveland-Lorain-Elyria, OH','Cleveland','OH','USA','41.4993','-81.6954',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(50,'Tampa-St. Petersburg-Clearwater, FL','Tampa','FL','USA','27.9475','-82.4584',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(51,'Anchorage, AK','Anchorage','AK','USA','66.1605','-153.3691',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(52,'Honolulu, HI','Honolulu','HI','USA','21.3156','-157.8580',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(53,'San Juan, PR','San Juan','PR','USA','18.4663','-66.1057',NULL,NULL,NULL,NULL,0);
INSERT INTO destinations VALUES(54,'Acadia National Park',NULL,'ME','USA','44.35','-68.21',NULL,NULL,'Boston-Cambridge-Nashua, MA-NH',NULL,0);
INSERT INTO destinations VALUES(55,'Asheville',NULL,'NC','USA','35.59','-82.55',NULL,NULL,'Greenville-Anderson-Mauldin, SC',NULL,0);
INSERT INTO destinations VALUES(56,'Bar Harbor',NULL,'ME','USA','44.39','-68.20',NULL,NULL,'Boston-Cambridge-Nashua, MA-NH',NULL,0);
INSERT INTO destinations VALUES(57,'Bend',NULL,'OR','USA','44.06','-121.31',NULL,NULL,'Portland-Vancouver-Hillsboro, OR-WA',NULL,0);
INSERT INTO destinations VALUES(58,'Big Sur',NULL,'CA','USA','36.22','-121.67',NULL,NULL,'San Jose-Sunnyvale-Santa Clara, CA',NULL,0);
INSERT INTO destinations VALUES(59,'Branson',NULL,'MO','USA','36.6439','-93.2183',NULL,NULL,'Tulsa, OK',NULL,0);
INSERT INTO destinations VALUES(60,'Breckenridge',NULL,'CO','USA','39.4822','-106.0382',NULL,NULL,'Denver-Aurora-Lakewood, CO',NULL,0);
INSERT INTO destinations VALUES(61,'Cape Cod',NULL,'MA','USA','41.9333','-70.0167',NULL,NULL,'Boston-Cambridge-Nashua, MA-NH',NULL,0);
INSERT INTO destinations VALUES(62,'Charleston',NULL,'SC','USA','32.7857','-79.9339',NULL,NULL,'Charlotte-Concord-Gastonia, NC-SC',NULL,0);
INSERT INTO destinations VALUES(63,'Cooperstown',NULL,'NY','USA','42.6978','-74.9239',NULL,NULL,'New York-Newark-Jersey City, NY-NJ-PA',NULL,0);
INSERT INTO destinations VALUES(64,'Custer State Park',NULL,'SD','USA','43.75','-103.43',NULL,NULL,'Denver-Aurora-Lakewood, CO',NULL,0);
INSERT INTO destinations VALUES(65,'Durango',NULL,'CO','USA','37.28','-107.88',NULL,NULL,'Denver-Aurora-Lakewood, CO',NULL,0);
INSERT INTO destinations VALUES(66,'Gatlinburg',NULL,'TN','USA','35.71','-83.52',NULL,NULL,'Greenville-Anderson-Mauldin, SC',NULL,0);
INSERT INTO destinations VALUES(67,'Glacier National Park',NULL,'MT','USA','48.77','-113.67',NULL,NULL,'Seattle-Tacoma-Bellevue, WA',NULL,0);
INSERT INTO destinations VALUES(68,'Glenwood Springs',NULL,'CO','USA','39.55','-107.32',NULL,NULL,'Denver-Aurora-Lakewood, CO',NULL,0);
INSERT INTO destinations VALUES(69,'Grand Canyon',NULL,'AZ','USA','36.0544','-112.1401',NULL,NULL,'Las Vegas-Henderson-Paradise, NV',NULL,0);
INSERT INTO destinations VALUES(70,'Great Smoky Mountains National Park',NULL,'TN','USA','35.6184','-83.5302',NULL,NULL,'Greenville-Anderson-Mauldin, SC',NULL,0);
INSERT INTO destinations VALUES(71,'Jackson Hole',NULL,'WY','USA','43.5825','-110.8219',NULL,NULL,'Denver-Aurora-Lakewood, CO',NULL,0);
INSERT INTO destinations VALUES(72,'Kauai',NULL,'HI','USA','22.0827','-159.4983',NULL,NULL,'Honolulu, HI',NULL,0);
INSERT INTO destinations VALUES(73,'Key West',NULL,'FL','USA','24.5551','-81.7801',NULL,NULL,'Miami-Fort Lauderdale-Pompano Beach, FL',NULL,0);
INSERT INTO destinations VALUES(74,'Lake Tahoe',NULL,'CA','USA','39.0942','-120.0424',NULL,NULL,'Sacramento-Roseville-Arden-Arcade, CA',NULL,0);
INSERT INTO destinations VALUES(75,'Mackinac Island',NULL,'MI','USA','45.8497','-84.6278',NULL,NULL,'Milwaukee-Waukesha-West Allis, WI',NULL,0);
INSERT INTO destinations VALUES(76,'Maui',NULL,'HI','USA','20.7984','-156.3314',NULL,NULL,'Honolulu, HI',NULL,0);
INSERT INTO destinations VALUES(77,'Mount Rushmore',NULL,'SD','USA','43.8794','-103.4597',NULL,NULL,'Denver-Aurora-Lakewood, CO',NULL,0);
INSERT INTO destinations VALUES(78,'Myrtle Beach',NULL,'SC','USA','33.6926','-78.8867',NULL,NULL,'Raleigh, NC',NULL,0);
INSERT INTO destinations VALUES(79,'Napa Valley',NULL,'CA','USA','38.2977','-122.2864',NULL,NULL,'Oakland-Hayward-Berkeley, CA',NULL,0);
INSERT INTO destinations VALUES(80,'Olympic National Park',NULL,'WA','USA','47.5714','-123.4431',NULL,NULL,'Seattle-Tacoma-Bellevue, WA',NULL,0);
INSERT INTO destinations VALUES(81,'Palm Springs',NULL,'CA','USA','33.8303','-116.5453',NULL,NULL,'San Diego-Carlsbad, CA',NULL,0);
INSERT INTO destinations VALUES(82,'Santa Fe',NULL,'NM','USA','35.6869','-105.9378',NULL,NULL,'El Paso, TX',NULL,0);
INSERT INTO destinations VALUES(83,'Savannah',NULL,'GA','USA','32.0835','-81.0998',NULL,NULL,'Jacksonville, FL',NULL,0);
INSERT INTO destinations VALUES(84,'Sedona',NULL,'AZ','USA','34.8697','-111.7603',NULL,NULL,'Phoenix-Mesa-Scottsdale, AZ',NULL,0);
INSERT INTO destinations VALUES(85,'St. Augustine',NULL,'FL','USA','29.8942','-81.3145',NULL,NULL,'Jacksonville, FL',NULL,0);
INSERT INTO destinations VALUES(86,'Telluride',NULL,'CO','USA','37.9375','-107.8206',NULL,NULL,'Denver-Aurora-Lakewood, CO',NULL,0);
INSERT INTO destinations VALUES(87,'Williamsburg',NULL,'VA','USA','37.2707','-76.7074',NULL,NULL,'Virginia Beach-Norfolk-Newport News, VA-NC',NULL,0);
INSERT INTO destinations VALUES(88,'Yellowstone National Park',NULL,'WY','USA','44.4275','-110.5885',NULL,NULL,'Denver-Aurora-Lakewood, CO',NULL,0);
INSERT INTO destinations VALUES(89,'Yosemite National Park',NULL,'CA','USA','37.7447','-119.5882',NULL,NULL,'Sacramento-Roseville-Arden-Arcade, CA',NULL,0);
INSERT INTO destinations VALUES(90,'Zion National Park',NULL,'UT','USA','37.2986','-113.0267',NULL,NULL,'Las Vegas-Henderson-Paradise, NV',NULL,0);
INSERT INTO destinations VALUES(91,'Amsterdam',NULL,NULL,'Netherlands','52.3702','4.8903',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(92,'Aruba Island',NULL,NULL,'Aruba','12.5079','-70.0353',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(93,'Athens',NULL,NULL,'Greece','37.9838','23.7275',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(94,'Auckland',NULL,NULL,'New Zealand','-36.8485','174.7633',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(95,'Bali',NULL,NULL,'Indonesia','-8.4095','115.1889',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(96,'Bangkok',NULL,NULL,'Thailand','13.7563','100.5018',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(97,'Barcelona',NULL,NULL,'Spain','41.3851','2.1734',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(98,'Beijing',NULL,NULL,'China','39.9042','116.3974',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(99,'Berlin',NULL,NULL,'Germany','52.5200','13.4050',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(100,'Bogota',NULL,NULL,'Colombia','4.6097','-74.0817',NULL,NULL,NULL,'Reconsider Travel',0);
INSERT INTO destinations VALUES(101,'Buenos Aires',NULL,NULL,'Argentina','-34.6037','-58.3816',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(102,'Cabo San Lucas',NULL,NULL,'Mexico','22.8869','-109.4253',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(103,'Cairo',NULL,NULL,'Egypt','30.0522','31.2497',NULL,NULL,NULL,'Reconsider Travel',0);
INSERT INTO destinations VALUES(104,'Cancun',NULL,NULL,'Mexico','21.1743','-86.8466',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(105,'Cape Town',NULL,NULL,'South Africa','-33.9249','18.4241',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(106,'Casablanca',NULL,NULL,'Morocco','33.5928','-7.9222',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(107,'Copenhagen',NULL,NULL,'Denmark','55.6763','12.5681',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(108,'Delhi',NULL,NULL,'India','28.6139','77.2090',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(109,'Dubai',NULL,NULL,'United Arab Emirates','25.0657','55.1713',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(110,'Dublin',NULL,NULL,'Ireland','53.3441','-6.2672',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(111,'Dubrovnik',NULL,NULL,'Croatia','42.6481','18.0921',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(112,'Edinburgh',NULL,NULL,'Scotland','55.9533','-3.1883',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(113,'George Town',NULL,NULL,'Cayman Islands','19.2937','-81.3865',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(114,'Hanoi',NULL,NULL,'Vietnam','21.0278','105.8342',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(115,'Helsinki',NULL,NULL,'Finland','60.1699','24.9384',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(116,'Ho Chi Minh City',NULL,NULL,'Vietnam','10.7626','106.6747',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(117,'Hong Kong',NULL,NULL,'China','22.3964','114.1095',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(118,'Istanbul',NULL,NULL,'Turkey','41.0082','28.9744',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(119,'Jerusalem',NULL,NULL,'Israel','31.7833','35.2167',NULL,NULL,NULL,'Reconsider Travel',0);
INSERT INTO destinations VALUES(120,'Kuala Lumpur',NULL,NULL,'Malaysia','3.1390','101.6869',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(121,'Lima',NULL,NULL,'Peru','-12.0464','-77.0428',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(122,'Lisbon',NULL,NULL,'Portugal','38.7223','-9.1393',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(123,'London',NULL,NULL,'England','51.5074','-0.1278',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(124,'Macau',NULL,NULL,'China','22.1667','113.5500',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(125,'Madrid',NULL,NULL,'Spain','40.4168','-3.7033',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(126,'Manila',NULL,NULL,'Philippines','14.5995','121.0817',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(127,'Marrakech',NULL,NULL,'Morocco','31.6295','-7.9811',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(128,'Mexico City',NULL,NULL,'Mexico','19.4326','-99.1332',NULL,NULL,NULL,'Reconsider Travel',0);
INSERT INTO destinations VALUES(129,'Montego Bay',NULL,NULL,'Jamaica','18.5093','-77.8947',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(130,'Montreal',NULL,NULL,'Canada','45.5017','-73.5673',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(131,'Moscow',NULL,NULL,'Russia','55.7558','37.6173',NULL,NULL,NULL,'Do Not Travel',0);
INSERT INTO destinations VALUES(132,'Mumbai',NULL,NULL,'India','19.0759','72.8777',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(133,'Nassau',NULL,NULL,'Bahamas','25.0582','-77.3434',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(134,'Oslo',NULL,NULL,'Norway','59.9139','10.7522',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(135,'Panama City',NULL,NULL,'Panama','9.0007','-79.5163',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(136,'Paris',NULL,NULL,'France','48.8567','2.3522',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(137,'Phuket',NULL,NULL,'Thailand','7.8906','98.3923',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(138,'Prague',NULL,NULL,'Czech Republic','50.0755','14.4378',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(139,'Puerto Vallarta',NULL,NULL,'Mexico','20.6773','-105.2447',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(140,'Punta Cana',NULL,NULL,'Dominican Republic','18.5667','-68.4167',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(141,'Reykjavik',NULL,NULL,'Iceland','64.1353','-21.8954',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(142,'Rio de Janeiro',NULL,NULL,'Brazil','-22.9068','-43.1729',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(143,'Rome',NULL,NULL,'Italy','41.8719','12.4964',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(144,'San Jose',NULL,NULL,'Costa Rica','9.9281','-84.0907',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(145,'San Salvador',NULL,NULL,'El Salvador','13.6892','-89.2012',NULL,NULL,NULL,'Reconsider Travel',0);
INSERT INTO destinations VALUES(146,'Santiago',NULL,NULL,'Chile','-33.4378','-70.6506',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(147,'Santorini',NULL,NULL,'Greece','36.3932','25.4597',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(148,'Seoul',NULL,NULL,'South Korea','37.5665','126.9778',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(149,'Shanghai',NULL,NULL,'China','31.2304','121.4737',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(150,'Singapore',NULL,NULL,'Singapore','1.3521','103.8198',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(151,'Split',NULL,NULL,'Croatia','43.5065','16.4439',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(152,'St. Petersburg',NULL,NULL,'Russia','59.9389','30.3256',NULL,NULL,NULL,'Do Not Travel',0);
INSERT INTO destinations VALUES(153,'Stockholm',NULL,NULL,'Sweden','59.3293','18.0686',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(154,'Sydney',NULL,NULL,'Australia','-33.8651','151.2099',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(155,'Taipei',NULL,NULL,'Taiwan','25.0478','121.5319',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(156,'Tel Aviv',NULL,NULL,'Israel','32.0853','34.7804',NULL,NULL,NULL,'Exercise Increased Precautions',0);
INSERT INTO destinations VALUES(157,'Tokyo',NULL,NULL,'Japan','35.6895','139.7670',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(158,'Toronto',NULL,NULL,'Canada','43.6532','-79.3832',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(159,'Vancouver',NULL,NULL,'Canada','49.2827','-123.1207',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(160,'Vienna',NULL,NULL,'Austria','48.2082','16.3738',NULL,NULL,NULL,'Exercise Normal Precautions',0);
INSERT INTO destinations VALUES(161,'Zurich',NULL,NULL,'Switzerland','47.3769','8.5382',NULL,NULL,NULL,'Exercise Normal Precautions',0);
CREATE TABLE hotels (id integer primary key autoincrement,
name varchar,
address varchar,
distance varchar,
star_rating varchar,
description varchar,
location_id integer,
foreign key (location_id) references locations(id)
);
INSERT INTO hotels VALUES(17,'The Langham Chicago','330 N Wabash Ave, Chicago, IL 60611','0.6','5','Luxurious hotel with elegant rooms, a fitness center, and a world-class spa, located in a historic building along the Chicago River.',3);
INSERT INTO hotels VALUES(18,'Trump International Hotel & Tower Chicago','401 N Wabash Ave, Chicago, IL 60611','0.7','5','Upscale hotel with modern rooms, a rooftop pool, and a Michelin-starred restaurant, located in a sleek skyscraper along the Chicago River.',3);
INSERT INTO hotels VALUES(19,'The Wit Hotel','201 N State St, Chicago, IL 60601','0.8','4','Trendy hotel with chic rooms, a rooftop bar, and a fitness center, located in the heart of the Loop, close to Millennium Park.',3);
INSERT INTO hotels VALUES(20,'Hyatt Centric The Loop Chicago','100 W Monroe St, Chicago, IL 60603','0.9','4','Modern hotel with stylish rooms, a rooftop pool, and a fitness center, located in the Loop, close to Willis Tower and the Chicago River.',3);
INSERT INTO hotels VALUES(21,'Kimpton Hotel Monaco Chicago','225 N Wabash Ave, Chicago, IL 60601','1.0','4','Boutique hotel with elegant rooms, a fitness center, and a complimentary wine hour, located in a historic building in the Loop.',3);
INSERT INTO hotels VALUES(22,'LondonHouse Chicago','85 E Wacker Dr, Chicago, IL 60601','1.1','4','Luxury hotel with modern rooms, a rooftop bar, and a fitness center, located in a historic building along the Chicago River.',3);
INSERT INTO hotels VALUES(23,'Renaissance Chicago Downtown Hotel','1 W Wacker Dr, Chicago, IL 60601','1.2','4','Upscale hotel with modern rooms, a fitness center, and an indoor pool, located in the Loop, close to Millennium Park.',3);
INSERT INTO hotels VALUES(24,'The Westin Chicago River North','320 N Dearborn St, Chicago, IL 60654','1.3','4','Modern hotel with comfortable rooms, a fitness center, and an indoor pool, located in the River North neighborhood, close to the Chicago River.',3);
INSERT INTO hotels VALUES(25,'Hotel EMC2, Autograph Collection','228 E Ontario St, Chicago, IL 60611','1.4','4','Boutique hotel with stylish rooms, a fitness center, and a rooftop lounge, located in the Streeterville neighborhood, close to Navy Pier.',3);
INSERT INTO hotels VALUES(26,'Loews Chicago Hotel','455 N Park Dr, Chicago, IL 60611','1.5','4','Upscale hotel with modern rooms, a fitness center, and an indoor pool, located in the Streeterville neighborhood, close to Navy Pier.',3);
INSERT INTO hotels VALUES(27,'The Ritz-Carlton, Chicago','160 E Pearson St, Chicago, IL 60611','0.6','5','Luxury hotel with elegant rooms, rooftop lounge, and upscale dining options, including a Michelin-starred restaurant.',3);
INSERT INTO hotels VALUES(28,'Four Seasons Hotel Chicago','120 E Delaware Pl, Chicago, IL 60611','0.7','5','Luxury hotel with modern rooms, rooftop pool, and upscale dining options, including a Michelin-starred restaurant.',3);
INSERT INTO hotels VALUES(29,'The Gwen, a Luxury Collection Hotel, Michigan Avenue Chicago','521 N Rush St, Chicago, IL 60611','0.8','4','Upscale hotel with modern rooms, rooftop lounge, and several dining options, including a restaurant and bar.',3);
INSERT INTO hotels VALUES(30,'The Westin Michigan Avenue Chicago','909 N Michigan Ave, Chicago, IL 60611','0.9','4','Upscale hotel with modern rooms, fitness center, and several dining options, including a restaurant and bar.',3);
INSERT INTO hotels VALUES(31,'Kimpton Hotel Allegro','171 W Randolph St, Chicago, IL 60601','1.2','4','Boutique hotel with stylish rooms, fitness center, and several dining options, including a restaurant and bar.',3);
INSERT INTO hotels VALUES(32,'Swissotel Chicago','323 E Wacker Dr, Chicago, IL 60601','1.2','4','Modern hotel with comfortable rooms, fitness center, and rooftop pool, located along the Chicago River.',3);
INSERT INTO hotels VALUES(33,'Hilton Chicago','720 S Michigan Ave, Chicago, IL 60605','1.4','4','Upscale hotel with comfortable rooms, fitness center, and rooftop pool, located in the South Loop neighborhood.',3);
CREATE TABLE room_rates (id integer primary key autoincrement, room_type varchar, room_description varchar, amenities varchar, winter_rate varchar, summer_rate varchar, cancellation_policy varchar, hotel_id integer, foreign key (hotel_id) references hotels(id));
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('hotels',33);
INSERT INTO sqlite_sequence VALUES('designations',161);
COMMIT;
