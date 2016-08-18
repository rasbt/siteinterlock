delete FlexClustObj
delete FC*
delete smallFC*
delete RC*
delete HPHOB3
load 1com_nolig_flex_0001.pdb, FlexClustObj


select FC1, FlexClustObj and id 3817-3859
color palegreen, FC1
show sticks, FC1
show cartoon, FC1
cartoon tube, FC1

select FC3, FlexClustObj and id 3866-3874
color paleyellow, FC3
show sticks, FC3
show cartoon, FC3
cartoon tube, FC3

select FC4, FlexClustObj and id 3875-3987
color lightpink, FC4
show sticks, FC4
show cartoon, FC4
cartoon tube, FC4

select FC5, FlexClustObj and id 3988-4004
color palecyan, FC5
show sticks, FC5
show cartoon, FC5
cartoon tube, FC5

select FC6, FlexClustObj and id 4005-4032
color lightorange, FC6
show sticks, FC6
show cartoon, FC6
cartoon tube, FC6

select FC7, FlexClustObj and id 4033-4044
color bluewhite, FC7
show sticks, FC7
show cartoon, FC7
cartoon tube, FC7

select FC9, FlexClustObj and id 4051-4058
color limegreen, FC9
show sticks, FC9
show cartoon, FC9
cartoon tube, FC9

select FC11, FlexClustObj and id 4065-4224
color slate, FC11
show sticks, FC11
show cartoon, FC11
cartoon tube, FC11

select FC12, FlexClustObj and id 4225-4236
color aquamarine, FC12
show sticks, FC12
show cartoon, FC12
cartoon tube, FC12

select FC13, FlexClustObj and id 4237-4244
color lightorange, FC13
show sticks, FC13
show cartoon, FC13
cartoon tube, FC13

select FC14, FlexClustObj and id 4245-4251
color sand, FC14
show sticks, FC14
show cartoon, FC14
cartoon tube, FC14

select smallFCs0, FlexClustObj and id 3860-3865+4045-4050+4059-4064
color brown, smallFCs0
show sticks, smallFCs0
show cartoon, smallFCs0
cartoon tube, smallFCs0



select RC, FlexClustObj and id 1-1708
color blue, RC
show lines, RC


select dangle, FlexClustObj and id 1709-3816
color white, dangle
show lines, dangle


select HPHOB3, FlexClustObj and resn "XXX" 
show spheres, HPHOB3
set sphere_scale=0.4
deselect HPHOB3
