'''
FORMAT
	course name : [prereqs, co-reqs, sections, exclusions]
'''
# prof rating (out of 6)
prof_rat = {"Alice" : 6, "Bob" : 5, "Chris" : 4, "Dave" : 3, "Ellen": 2, "Frank" : 1, "Georgia" : 0}

# all courses with their info
dat = {"CSC108": [[], [], [((1,'M','M',"Alice"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Dave"),),((1,'F','D',"Chris"),), ((1,'J','N',"Chris"),), ((2,'T','M',"Bob"),), ((3,'W','N',"Bob"),)], []],
		######
		"CSC148": [["CSC108"], [], [((2,'M','E',"Bob"),), ((3,'M','M',"Alice"),), ((2,'M','N',"Chris"),), ((3,'F','M',"Dave"),), ((4,'J','M',"Alice"),), ((4,'M','M',"Bob"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		######
		"CSC165": [[], [], [((1,'M','D',"Ellen"),), ((3,'M','M',"Bob"),), ((1,'M','N',"Bob"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Dave"),), ((1,'W','N',"Chris"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Bob"),)], []],
		######
		"CSC207": [["CSC148"], [], [((2,'M','E',"Bob"),), ((3,'M','M',"Bob"),), ((2,'M','N',"Bob"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Chris"),), ((1,'F','M',"Alice"),), ((4,'W','N',"Alice"),), ((3,'F','E',"Ellen"),), ((5,'F','D',"Dave"),)], []],
		######
		"CSC209": [["CSC207"], [], [((2,'M','E',"Dave"),), ((3,'M','M',"Dave"),), ((2,'M','N',"Dave"),), ((3,'F','M',"Dave"),), ((5,'J','M',"Alice"),), ((5,'M','M',"Alice"),), ((5,'W','M',"Alice"),), ((2,'T','N',"Chris"),), ((3,'J','N',"Chris"),)], []],
		######
		"CSC236": [["CSC165"], [], [((2,'M','E',"Chris"),), ((3,'M','M',"Chris"),), ((2,'M','N',"Frank"),), ((3,'F','M',"Frank"),), ((4,'J','M',"Frank"),), ((1,'M','M',"Georgia"),), ((1,'W','N',"Georgia"),), ((2,'T','E',"Bob"),), ((3,'F','D',"Bob"),)], []],
		######
		"CSC263": [["CSC236", "CSC207"], [], [((3,'M','E',"Chris"),), ((4,'M','M',"Chris"),), ((3,'M','N',"Chris"),), ((4,'F','M',"Chris"),), ((5,'J','M',"Alice"),), ((2,'M','M',"Frank"),), ((2,'W','N',"Georgia"),), ((3,'T','E',"Georgia"),), ((4,'F','D',"Frank"),)], []],
		######
		"CSC258": [["CSC148"], [], [((3,'M','E',"Frank"),), ((4,'M','M',"Frank"),), ((3,'M','N',"Alice"),), ((4,'F','M',"Chris"),), ((5,'J','M',"Chris"),), ((5,'M','M',"Dave"),), ((2,'W','N',"Dave"),), ((3,'T','E',"Dave"),), ((4,'F','D',"Alice"),)], []],
		######
		"MAT137": [[], ["CSC148","CSC165"], [((1,'M','E',"Alice"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Ellen"),), ((1,'M','M',"Chris"),), ((1,'W','N',"Frank"),), ((2,'T','E',"Frank"),), ((3,'F','D',"Georgia"),)], ["MAT135"]],
		######
		"MAT135": [[], ["CSC148"], [((1,'M','E',"Georgia"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Bob"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], ["MAT137"]],
		######
		"CSC104": [[], [], [((2,'M','E',"Ellen"),), ((3,'M','M',"Alice"),), ((2,'M','N',"Chris"),), ((3,'F','M',"Dave"),), ((4,'J','M',"Alice"),), ((4,'M','M',"Bob"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		######
		"CSC120": [[], [], [((1,'M','D',"Chris"),), ((3,'M','M',"Bob"),), ((1,'M','N',"Bob"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Dave"),), ((1,'W','N',"Chris"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Bob"),)], []],
		######
		"CSC121": [[], [], [((2,'M','E',"Bob"),), ((3,'M','M',"Bob"),), ((2,'M','N',"Bob"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Chris"),), ((1,'F','M',"Alice"),), ((4,'W','N',"Alice"),), ((3,'F','E',"Alice"),), ((5,'F','D',"Dave"),)], []],
		######
		"CSC204": [["CSC207"], [], [((2,'M','E',"Dave"),), ((3,'M','M',"Dave"),), ((2,'M','N',"Dave"),), ((3,'F','M',"Dave"),), ((5,'J','M',"Alice"),), ((5,'M','M',"Alice"),), ((5,'W','M',"Alice"),), ((2,'T','N',"Chris"),), ((3,'J','N',"Chris"),)], []],
		######
		"CSC300": [[], [], [((5,'M','E',"Chris"),), ((6,'M','M',"Chris"),), ((5,'M','N',"Chris"),), ((6,'F','M',"Chris"),), ((7,'J','M',"Alice"),), ((4,'M','M',"Frank"),), ((4,'W','N',"Georgia"),), ((5,'T','E',"Georgia"),), ((6,'F','D',"Frank"),), ((8,'M','E',"Chris"),), ((9,'M','M',"Chris"),), ((8,'M','N',"Chris"),), ((9,'F','M',"Chris"),), ((10,'J','M',"Alice"),), ((7,'M','M',"Frank"),), ((7,'W','N',"Georgia"),), ((8,'T','E',"Georgia"),), ((9,'F','D',"Frank"),)], []],
		######
		"CSC301": [["CSC148", "CSC263"], [], [((5,'M','E',"Frank"),), ((6,'M','M',"Frank"),), ((5,'M','N',"Alice"),), ((6,'F','M',"Chris"),), ((5,'J','M',"Chris"),), ((4,'M','M',"Dave"),), ((1,'W','N',"Dave"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Alice"),)], []],
		######
		"CSC302": [["CSC301"], [], [((1,'M','E',"Alice"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Chris"),), ((1,'M','M',"Chris"),), ((1,'W','N',"Frank"),), ((2,'T','E',"Frank"),), ((3,'F','D',"Georgia"),)], []],
		######
		"CSC304": [["CSC373"], [], [((1,'M','E',"Georgia"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Ellen"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		###### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		"CSC309": [["CSC209"], ["CSC343"], [((1,'M','M',"Alice"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Dave"),),((1,'F','D',"Chris"),), ((1,'J','N',"Chris"),), ((2,'T','M',"Bob"),), ((3,'W','N',"Bob"),)], []],
		######
		"CSC310": [["CSC148"], [], [((2,'M','E',"Bob"),), ((3,'M','M',"Alice"),), ((2,'M','N',"Chris"),), ((3,'F','M',"Dave"),), ((4,'J','M',"Alice"),), ((4,'M','M',"Bob"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		######
		"CSC318": [[], [], [((1,'M','D',"Chris"),), ((3,'M','M',"Bob"),), ((1,'M','N',"Bob"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Dave"),), ((1,'W','N',"Chris"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Ellen"),)], []],
		######
		"CSC320": [["CSC209"], [], [((2,'M','E',"Bob"),), ((3,'M','M',"Bob"),), ((2,'M','N',"Bob"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Chris"),), ((1,'F','M',"Alice"),), ((4,'W','N',"Alice"),), ((3,'F','E',"Alice"),), ((5,'F','D',"Dave"),)], []],
		######
		"CSC321": [["MAT137"], [], [((2,'M','E',"Dave"),), ((3,'M','M',"Dave"),), ((2,'M','N',"Dave"),), ((3,'F','M',"Dave"),), ((5,'J','M',"Alice"),), ((5,'M','M',"Alice"),), ((5,'W','M',"Alice"),), ((2,'T','N',"Chris"),), ((3,'J','N',"Chris"),)], []],
		######
		"CSC324": [["CSC263"], [], [((2,'M','E',"Chris"),), ((3,'M','M',"Chris"),), ((2,'M','N',"Frank"),), ((3,'F','M',"Frank"),), ((4,'J','M',"Frank"),), ((1,'M','M',"Georgia"),), ((1,'W','N',"Georgia"),), ((2,'T','E',"Bob"),), ((3,'F','D',"Bob"),)], []],
		######
		"CSC336": [["CSC148"], [], [((2,'M','E',"Chris"),), ((3,'M','M',"Chris"),), ((2,'M','N',"Chris"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Frank"),), ((1,'W','N',"Georgia"),), ((2,'T','E',"Georgia"),), ((3,'F','D',"Frank"),)], []],
		######
		"CSC343": [["CSC165", "CSC207"], [], [((2,'M','E',"Frank"),), ((3,'M','M',"Frank"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Chris"),), ((4,'M','M',"Dave"),), ((1,'W','N',"Dave"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Alice"),)], []],
		######
		"CSC358": [["CSC209", "CSC258", "CSC263"], [], [((1,'M','E',"Alice"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Chris"),), ((1,'M','M',"Chris"),), ((1,'W','N',"Frank"),), ((2,'T','E',"Frank"),), ((3,'F','D',"Georgia"),)], []],
		######
		"CSC367": [["CSC258", "CSC209"], [], [((1,'M','E',"Georgia"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Bob"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		###### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		"CSC369": [["CSC258", "CSC209"], [], [((1,'M','M',"Alice"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Dave"),),((1,'F','D',"Chris"),), ((1,'J','N',"Chris"),), ((2,'T','M',"Bob"),), ((3,'W','N',"Bob"),)], []],
		######
		"CSC373": [["CSC263"], [], [((2,'M','E',"Bob"),), ((3,'M','M',"Alice"),), ((2,'M','N',"Chris"),), ((3,'F','M',"Dave"),), ((4,'J','M',"Alice"),), ((4,'M','M',"Ellen"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		######
		"CSC384": [["CSC263"], [], [((1,'M','D',"Chris"),), ((3,'M','M',"Bob"),), ((1,'M','N',"Bob"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Dave"),), ((1,'W','N',"Chris"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Bob"),)], []],
		######
		"CSC385": [["CSC258", "CSC209"], [], [((2,'M','E',"Bob"),), ((3,'M','M',"Bob"),), ((2,'M','N',"Bob"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Chris"),), ((1,'F','M',"Alice"),), ((4,'W','N',"Alice"),), ((3,'F','E',"Alice"),), ((5,'F','D',"Dave"),)], []],
		######
		"CSC396": [["CSC207"], [], [((2,'M','E',"Dave"),), ((3,'M','M',"Dave"),), ((2,'M','N',"Dave"),), ((3,'F','M',"Dave"),), ((5,'J','M',"Alice"),), ((5,'M','M',"Alice"),), ((5,'W','M',"Alice"),), ((2,'T','N',"Chris"),), ((3,'J','N',"Chris"),)], []],
		######
		"CSC401": [["CSC207"], [], [((2,'M','E',"Chris"),), ((3,'M','M',"Chris"),), ((2,'M','N',"Frank"),), ((3,'F','M',"Frank"),), ((4,'J','M',"Frank"),), ((1,'M','M',"Georgia"),), ((1,'W','N',"Georgia"),), ((2,'T','E',"Ellen"),), ((3,'F','D',"Bob"),)], []],
		######
		"CSC404": [["CSC301"], [], [((2,'M','E',"Chris"),), ((3,'M','M',"Chris"),), ((2,'M','N',"Chris"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Frank"),), ((1,'W','N',"Georgia"),), ((2,'T','E',"Georgia"),), ((3,'F','D',"Frank"),)], []],
		######
		"CSC410": [["CSC207", "CSC236"], [], [((2,'M','E',"Frank"),), ((3,'M','M',"Frank"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Chris"),), ((4,'M','M',"Dave"),), ((1,'W','N',"Dave"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Alice"),)], []],
		######
		"CSC411": [["CSC236"], [], [((1,'M','E',"Alice"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Chris"),), ((1,'M','M',"Chris"),), ((1,'W','N',"Frank"),), ((2,'T','E',"Frank"),), ((3,'F','D',"Georgia"),)], []],
		######
		"CSC412": [["CSC411"], [], [((1,'M','E',"Georgia"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Bob"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		###### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		"CSC418": [["CSC336"], [], [((1,'M','M',"Alice"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Dave"),),((1,'F','D',"Chris"),), ((1,'J','N',"Chris"),), ((2,'T','M',"Bob"),), ((3,'W','N',"Ellen"),)], []],
		######
		"CSC420": [["CSC263"], [], [((2,'M','E',"Bob"),), ((3,'M','M',"Alice"),), ((2,'M','N',"Chris"),), ((3,'F','M',"Dave"),), ((4,'J','M',"Alice"),), ((4,'M','M',"Bob"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		######
		"CSC428": [["CSC318"], [], [((1,'M','D',"Chris"),), ((3,'M','M',"Bob"),), ((1,'M','N',"Bob"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Dave"),), ((1,'W','N',"Chris"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Bob"),)], []],
		######
		"CSC436": [["CSC336"], [], [((2,'M','E',"Bob"),), ((3,'M','M',"Bob"),), ((2,'M','N',"Bob"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Chris"),), ((1,'F','M',"Alice"),), ((4,'W','N',"Alice"),), ((3,'F','E',"Alice"),), ((5,'F','D',"Dave"),)], []],
		######
		"CSC438": [["CSC373"], [], [((2,'M','E',"Dave"),), ((3,'M','M',"Dave"),), ((2,'M','N',"Dave"),), ((3,'F','M',"Dave"),), ((5,'J','M',"Alice"),), ((5,'M','M',"Alice"),), ((5,'W','M',"Alice"),), ((2,'T','N',"Chris"),), ((3,'J','N',"Chris"),)], []],
		######
		"CSC443": [["CSC343", "CSC369", "CSC373"], [], [((2,'M','E',"Chris"),), ((3,'M','M',"Chris"),), ((2,'M','N',"Frank"),), ((3,'F','M',"Frank"),), ((4,'J','M',"Frank"),), ((1,'M','M',"Georgia"),), ((1,'W','N',"Georgia"),), ((2,'T','E',"Ellen"),), ((3,'F','D',"Bob"),)], []],
		######
		"CSC446": [["CSC336"], [], [((2,'M','E',"Chris"),), ((3,'M','M',"Chris"),), ((2,'M','N',"Chris"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Frank"),), ((1,'W','N',"Georgia"),), ((2,'T','E',"Georgia"),), ((3,'F','D',"Frank"),)], []],
		######
		"CSC448": [["CSC263"], [], [((2,'M','E',"Frank"),), ((3,'M','M',"Frank"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Chris"),), ((4,'M','M',"Dave"),), ((1,'W','N',"Dave"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Alice"),)], []],
		######
		"CSC454": [[], [], [((1,'M','E',"Alice"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Chris"),), ((1,'M','M',"Chris"),), ((1,'W','N',"Frank"),), ((2,'T','E',"Frank"),), ((3,'F','D',"Georgia"),)], []],
		######
		"CSC456": [["CSC436"], [], [((1,'M','E',"Georgia"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Bob"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		###### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		"CSC458": [["CSC343", "CSC369", "CSC373"], [], [((1,'M','M',"Alice"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Dave"),),((1,'F','D',"Chris"),), ((1,'J','N',"Chris"),), ((2,'T','M',"Bob"),), ((3,'W','N',"Bob"),)], []],
		######
		"CSC463": [["CSC236"], [], [((2,'M','E',"Ellen"),), ((3,'M','M',"Alice"),), ((2,'M','N',"Chris"),), ((3,'F','M',"Dave"),), ((4,'J','M',"Alice"),), ((4,'M','M',"Bob"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		######
		"CSC465": [["CSC236"], [], [((1,'M','D',"Chris"),), ((3,'M','M',"Bob"),), ((1,'M','N',"Bob"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Dave"),), ((1,'W','N',"Chris"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Bob"),)], []],
		######
		"CSC466": [["CSC336"], [], [((2,'M','E',"Ellen"),), ((3,'M','M',"Bob"),), ((2,'M','N',"Bob"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Chris"),), ((1,'F','M',"Alice"),), ((4,'W','N',"Alice"),), ((3,'F','E',"Alice"),), ((5,'F','D',"Dave"),)], []],
		######
		"CSC469": [["CSC369"], [], [((2,'M','E',"Dave"),), ((3,'M','M',"Dave"),), ((2,'M','N',"Dave"),), ((3,'F','M',"Dave"),), ((5,'J','M',"Alice"),), ((5,'M','M',"Alice"),), ((5,'W','M',"Alice"),), ((2,'T','N',"Chris"),), ((3,'J','N',"Chris"),)], []],
		######
		"CSC473": [["CSC373"], [], [((2,'M','E',"Chris"),), ((3,'M','M',"Chris"),), ((2,'M','N',"Frank"),), ((3,'F','M',"Frank"),), ((4,'J','M',"Frank"),), ((1,'M','M',"Georgia"),), ((1,'W','N',"Georgia"),), ((2,'T','E',"Bob"),), ((3,'F','D',"Bob"),)], []],
		######
		"CSC485": [["CSC207"], [], [((2,'M','E',"Chris"),), ((3,'M','M',"Chris"),), ((2,'M','N',"Chris"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Frank"),), ((1,'W','N',"Georgia"),), ((2,'T','E',"Georgia"),), ((3,'F','D',"Frank"),)], []],
		######
		"CSC486": [["CSC384", "CSC373"], [], [((2,'M','E',"Frank"),), ((3,'M','M',"Frank"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Chris"),), ((4,'J','M',"Chris"),), ((4,'M','M',"Dave"),), ((1,'W','N',"Dave"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Alice"),)], []],
		######
		"CSC488": [["CSC258", "CSC263"], [], [((1,'M','E',"Alice"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Ellen"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Chris"),), ((1,'M','M',"Chris"),), ((1,'W','N',"Frank"),), ((2,'T','E',"Frank"),), ((3,'F','D',"Georgia"),)], []],
		######
		"CSC490": [[], [], [((1,'M','E',"Georgia"),), ((5,'M','M',"Alice"),), ((2,'M','N',"Alice"),), ((3,'F','M',"Ellen"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Bob"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		###### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		"CSC491": [[], [], [((1,'M','M',"Alice"),), ((1,'W','N',"Ellen"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Dave"),),((1,'F','D',"Chris"),), ((1,'J','N',"Chris"),), ((2,'T','M',"Bob"),), ((3,'W','N',"Bob"),)], []],
		######
		"CSC494": [[], [], [((2,'M','E',"Bob"),), ((3,'M','M',"Alice"),), ((2,'M','N',"Chris"),), ((3,'F','M',"Dave"),), ((4,'J','M',"Alice"),), ((4,'M','M',"Bob"),), ((1,'W','N',"Bob"),), ((2,'T','E',"Dave"),), ((3,'F','D',"Dave"),)], []],
		######
		"CSC495": [[], [], [((1,'M','D',"Chris"),), ((3,'M','M',"Bob"),), ((1,'M','N',"Bob"),), ((3,'F','M',"Alice"),), ((4,'J','M',"Alice"),), ((1,'M','M',"Dave"),), ((1,'W','N',"Chris"),), ((2,'T','E',"Alice"),), ((3,'F','D',"Bob"),)], []]
		}
