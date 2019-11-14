INSERT INTO boss VALUES (1, 'boss', 'Edward Xu', 'edwardxu800422', 35000, '1980-04-22');
INSERT INTO boss VALUES (2, 'boss', 'Michelle Gu', 'michellegu820910', 35000, '1982-09-10');


INSERT INTO boss_phone VALUES (1, '13680042266');
INSERT INTO boss_phone VALUES (1, '86056666');
INSERT INTO boss_phone VALUES (2, '13982091088');
INSERT INTO boss_phone VALUES (2, '86058888');

INSERT INTO projectmanager VALUES (1, 'projectmanager', 'yifanlan', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 11000, '1992-01-01', 'Chengdu', 1);
INSERT INTO projectmanager VALUES (2, 'projectmanager', 'Mary Chen', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 11000, '1993-02-02','Guangzhou', 1);
INSERT INTO projectmanager VALUES (3, 'projectmanager', 'John Feng', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 11000, '1994-03-03', 'Shenzhen', 2);
INSERT INTO projectmanager VALUES (4, 'projectmanager', 'Linda Wu', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 11000, '1993-01-23','Yilake', 2);
INSERT INTO projectmanager VALUES (5, 'projectmanager', 'Patricia Lin', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'senior', 15000, '1989-04-04','England', 1);
INSERT INTO projectmanager VALUES (6, 'projectmanager', 'Robert Zhou', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'senior', 15000, '1987-05-05', 'America',2);


INSERT INTO projectmanager_phone VALUES (1, '13623478987');
INSERT INTO projectmanager_phone VALUES (1, '86050123');
INSERT INTO projectmanager_phone VALUES (2, '13678923432');
INSERT INTO projectmanager_phone VALUES (2, '86050234');
INSERT INTO projectmanager_phone VALUES (3, '13645632123');
INSERT INTO projectmanager_phone VALUES (3, '86050345');
INSERT INTO projectmanager_phone VALUES (4, '13667834543');
INSERT INTO projectmanager_phone VALUES (4, '86050456');
INSERT INTO projectmanager_phone VALUES (5, '13701023456');
INSERT INTO projectmanager_phone VALUES (5, '86050567');
INSERT INTO projectmanager_phone VALUES (6, '13702034567');
INSERT INTO projectmanager_phone VALUES (6, '86050678');


INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid) VALUES (1, '2019-02-01', 'complete', 14, 688, 'window of the world', 'wedding', 9, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (2, '2019-02-02', 'complete', 21, 988, 'cuhk(sz)', 'art', 8, 5);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (3, '2019-02-04', 'complete', 14, 688, 'happy valley', 'business', 8, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (4, '2019-02-05', 'complete', 7, 388, 'shenzhen bay', 'art', 8, 3);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (5, '2019-02-06', 'complete', 21, 988, 'shenzhen middle school', 'wedding', 9, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (6, '2019-02-06', 'complete', 7, 388, 'xiangmi park', 'wedding', 9, 4);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (7, '2019-02-08', 'complete', 14, 688, 'oct', 'art', 9, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (8, '2019-02-09', 'complete', 14, 688, 'dafen village', 'art', 7, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (9, '2019-02-11', 'complete', 21, 988, 'tencent headquarter', 'business', 8, 5);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (10, '2019-02-11', 'complete', 7, 388, 'coco park', 'wedding', 9, 3);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid) VALUES (11, '2019-03-01', 'after effect', 14, 688, 'window of the world', 'wedding', 9, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (12, '2019-03-02', 'taking photo', 21, 988, 'cuhk(sz)', 'art', 8, 5);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (13, '2019-03-04', 'taking photo', 14, 688, 'happy valley', 'business', 8, 2);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (14, '2019-03-05', 'after effect', 7, 388, 'shenzhen bay', 'art', 8, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (15, '2019-03-06', 'taking photo', 21, 988, 'shenzhen middle school', 'wedding', 9, 6);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (16, '2019-03-06', 'after effect', 7, 388, 'xiangmi park', 'wedding', 9, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (17, '2019-03-08', 'taking photo', 14, 688, 'oct', 'art', 9, 1);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (18, '2019-03-09', 'preparing', 14, 688, 'dafen village', 'art', 7, 2);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (19, '2019-03-11', 'preparing', 21, 988, 'tencent headquarter', 'business', 8, 5);
INSERT INTO porder (orderid, startdate, status, expectduration, price, place, ordertype, satisfaction, managerid)VALUES (20, '2019-03-11', 'preparing', 7, 388, 'coco park', 'wedding', 9, 1);

INSERT INTO photographer VALUES (1, 'photographer', 'wenjingcai', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 8000, '1995-01-17', 'Shenzhen');
INSERT INTO photographer VALUES (2, 'photographer', 'Barbara Yang', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 8000, '1995-02-08', 'Beijing');
INSERT INTO photographer VALUES (3, 'photographer', 'William Li', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 8000, '1996-03-25', 'Wuhan');
INSERT INTO photographer VALUES (4, 'photographer', 'Elizabeth Xia', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 8000, '1994-04-07', 'Japan');
INSERT INTO photographer VALUES (5, 'photographer', 'David Ma', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 8000, '1994-05-16', 'New York');
INSERT INTO photographer VALUES (6, 'photographer', 'Jennifer Luo', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'senior', 12000, '1992-06-23', 'Dujiangyan');
INSERT INTO photographer VALUES (7, 'photographer', 'Richard Song', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'senior', 12000, '1991-07-09', 'Tianjin');
INSERT INTO photographer VALUES (8, 'photographer', 'Maria Shen', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'senior', 12000, '1990-08-11', 'Japan');
INSERT INTO photographer VALUES (8, 'photographer', 'Maria Shen', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'senior', 12000, '1990-08-11', 'Japan');


INSERT INTO photographer_phone VALUES (1, '13601171234');
INSERT INTO photographer_phone VALUES (2, '13702082345');
INSERT INTO photographer_phone VALUES (3, '13803253456');
INSERT INTO photographer_phone VALUES (4, '13904074567');
INSERT INTO photographer_phone VALUES (5, '13605165678');
INSERT INTO photographer_phone VALUES (6, '13706236789');
INSERT INTO photographer_phone VALUES (7, '13807097890');
INSERT INTO photographer_phone VALUES (8, '13908118901');


INSERT INTO takephoto VALUES (1, 1);
INSERT INTO takephoto VALUES (1, 2);
INSERT INTO takephoto VALUES (2, 6);
INSERT INTO takephoto VALUES (2, 3);
INSERT INTO takephoto VALUES (2, 4);
INSERT INTO takephoto VALUES (3, 5);
INSERT INTO takephoto VALUES (3, 1);
INSERT INTO takephoto VALUES (4, 2);
INSERT INTO takephoto VALUES (5, 7);
INSERT INTO takephoto VALUES (5, 3);
INSERT INTO takephoto VALUES (5, 4);
INSERT INTO takephoto VALUES (6, 5);
INSERT INTO takephoto VALUES (7, 1);
INSERT INTO takephoto VALUES (7, 2);
INSERT INTO takephoto VALUES (8, 3);
INSERT INTO takephoto VALUES (8, 4);
INSERT INTO takephoto VALUES (9, 8);
INSERT INTO takephoto VALUES (9, 5);
INSERT INTO takephoto VALUES (9, 1);
INSERT INTO takephoto VALUES (10, 2);
INSERT INTO takephoto VALUES (11, 1);
INSERT INTO takephoto VALUES (11, 2);
INSERT INTO takephoto VALUES (12, 6);
INSERT INTO takephoto VALUES (12, 3);
INSERT INTO takephoto VALUES (12, 4);
INSERT INTO takephoto VALUES (13, 5);
INSERT INTO takephoto VALUES (13, 1);
INSERT INTO takephoto VALUES (14, 2);
INSERT INTO takephoto VALUES (15, 7);
INSERT INTO takephoto VALUES (15, 1);
INSERT INTO takephoto VALUES (15, 4);
INSERT INTO takephoto VALUES (16, 5);
INSERT INTO takephoto VALUES (17, 1);
INSERT INTO takephoto VALUES (17, 2);
INSERT INTO takephoto VALUES (18, 1);
INSERT INTO takephoto VALUES (18, 4);
INSERT INTO takephoto VALUES (19, 8);
INSERT INTO takephoto VALUES (19, 5);
INSERT INTO takephoto VALUES (19, 1);
INSERT INTO takephoto VALUES (20, 2);

INSERT INTO aftereffect VALUES (1, 'aftereffect', 'Charles An', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 6000, '1995-09-09', 'Guangzhou');
INSERT INTO aftereffect VALUES (2, 'aftereffect', 'Susan Bao', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 6000, '1996-10-18', 'Beijing');
INSERT INTO aftereffect VALUES (3, 'aftereffect', 'Joseph Cai', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 6000, '1995-11-25', 'Chengdu');
INSERT INTO aftereffect VALUES (4, 'aftereffect', 'Margaret Deng', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 6000, '1996-12-30', 'Japan');
INSERT INTO aftereffect VALUES (5, 'aftereffect', 'Thomas Fang', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'junior', 6000, '1994-01-27', 'America');
INSERT INTO aftereffect VALUES (6, 'aftereffect', 'Dorothy Gao', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'senior', 9000, '1989-02-13', 'Canada');
INSERT INTO aftereffect VALUES (7, 'aftereffect', 'Christopher Han', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'senior', 9000, '1988-03-04', 'India');
INSERT INTO aftereffect VALUES (8, 'aftereffect', 'Lisa Jiang', 'pbkdf2:sha256:150000$IceVsG42$ce77ce1dc9a2dc348930c7031733845e84b3012328bd977772a44644b77b9639', 'senior', 9000, '1990-04-30', 'India');


INSERT INTO aftereffect_phone VALUES (1, '13609094321');
INSERT INTO aftereffect_phone VALUES (2, '13710185432');
INSERT INTO aftereffect_phone VALUES (3, '13811256543');
INSERT INTO aftereffect_phone VALUES (4, '13912307654');
INSERT INTO aftereffect_phone VALUES (5, '13601278765');
INSERT INTO aftereffect_phone VALUES (6, '13702139876');
INSERT INTO aftereffect_phone VALUES (7, '13803040987');
INSERT INTO aftereffect_phone VALUES (8, '13904301098');


INSERT INTO doeffect VALUES (1, 4);
INSERT INTO doeffect VALUES (1, 5);
INSERT INTO doeffect VALUES (2, 8);
INSERT INTO doeffect VALUES (2, 2);
INSERT INTO doeffect VALUES (2, 3);
INSERT INTO doeffect VALUES (3, 1);
INSERT INTO doeffect VALUES (3, 4);
INSERT INTO doeffect VALUES (4, 5);
INSERT INTO doeffect VALUES (5, 7);
INSERT INTO doeffect VALUES (5, 2);
INSERT INTO doeffect VALUES (5, 3);
INSERT INTO doeffect VALUES (6, 1);
INSERT INTO doeffect VALUES (7, 4);
INSERT INTO doeffect VALUES (7, 5);
INSERT INTO doeffect VALUES (8, 2);
INSERT INTO doeffect VALUES (8, 3);
INSERT INTO doeffect VALUES (9, 6);
INSERT INTO doeffect VALUES (9, 1);
INSERT INTO doeffect VALUES (9, 4);
INSERT INTO doeffect VALUES (10, 5);
INSERT INTO doeffect VALUES (11, 4);
INSERT INTO doeffect VALUES (11, 5);
INSERT INTO doeffect VALUES (12, 8);
INSERT INTO doeffect VALUES (12, 2);
INSERT INTO doeffect VALUES (12, 3);
INSERT INTO doeffect VALUES (13, 1);
INSERT INTO doeffect VALUES (13, 4);
INSERT INTO doeffect VALUES (14, 5);
INSERT INTO doeffect VALUES (15, 7);
INSERT INTO doeffect VALUES (15, 2);
INSERT INTO doeffect VALUES (15, 3);
INSERT INTO doeffect VALUES (16, 1);
INSERT INTO doeffect VALUES (17, 4);
INSERT INTO doeffect VALUES (17, 5);
INSERT INTO doeffect VALUES (18, 2);
INSERT INTO doeffect VALUES (18, 3);
INSERT INTO doeffect VALUES (19, 6);
INSERT INTO doeffect VALUES (19, 1);
INSERT INTO doeffect VALUES (19, 4);
INSERT INTO doeffect VALUES (20, 5);


INSERT INTO devicemanager VALUES (1, 'device manager', 'Daniel Kang', 'danielkang960531', 'junior', 5000, '1996-05-31');
INSERT INTO devicemanager VALUES (2, 'device manager', 'Paul Liu', 'paulliu950622', 'junior', 5000, '1995-06-22');
INSERT INTO devicemanager VALUES (3, 'device manager', 'Mark Meng', 'markmeng920716', 'senior', 8000, '1992-07-16');


INSERT INTO devicemanager_phone VALUES (1, '13605316666');
INSERT INTO devicemanager_phone VALUES (2, '13706227777');
INSERT INTO devicemanager_phone VALUES (3, '13807168888');
