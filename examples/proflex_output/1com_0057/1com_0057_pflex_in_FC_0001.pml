delete FlexClustObj
delete FC*
delete smallFC*
delete RC*
delete HPHOB3
load 1com_0057_pflex_in_flex_0001.pdb, FlexClustObj


select FC1, FlexClustObj and id 3893-3935
color palegreen, FC1
show sticks, FC1
show cartoon, FC1
cartoon tube, FC1

select FC3, FlexClustObj and id 3942-3950
color paleyellow, FC3
show sticks, FC3
show cartoon, FC3
cartoon tube, FC3

select FC4, FlexClustObj and id 3951-3962
color lightpink, FC4
show sticks, FC4
show cartoon, FC4
cartoon tube, FC4

select FC5, FlexClustObj and id 3963-3979
color palecyan, FC5
show sticks, FC5
show cartoon, FC5
cartoon tube, FC5

select FC7, FlexClustObj and id 3986-3998
color bluewhite, FC7
show sticks, FC7
show cartoon, FC7
cartoon tube, FC7

select FC8, FlexClustObj and id 3999-4025
color teal, FC8
show sticks, FC8
show cartoon, FC8
cartoon tube, FC8

select FC10, FlexClustObj and id 4032-4059
color pink, FC10
show sticks, FC10
show cartoon, FC10
cartoon tube, FC10

select FC11, FlexClustObj and id 4060-4080
color slate, FC11
show sticks, FC11
show cartoon, FC11
cartoon tube, FC11

select FC12, FlexClustObj and id 4081-4092
color aquamarine, FC12
show sticks, FC12
show cartoon, FC12
cartoon tube, FC12

select FC14, FlexClustObj and id 4099-4106
color sand, FC14
show sticks, FC14
show cartoon, FC14
cartoon tube, FC14

select FC16, FlexClustObj and id 4113-4272
color lime, FC16
show sticks, FC16
show cartoon, FC16
cartoon tube, FC16

select FC17, FlexClustObj and id 4273-4284
color marine, FC17
show sticks, FC17
show cartoon, FC17
cartoon tube, FC17

select FC18, FlexClustObj and id 4285-4292
color splitpea, FC18
show sticks, FC18
show cartoon, FC18
cartoon tube, FC18

select FC19, FlexClustObj and id 4293-4299
color salmon, FC19
show sticks, FC19
show cartoon, FC19
cartoon tube, FC19

select smallFCs0, FlexClustObj and id 3936-3941+3980-3985+4026-4031+4093-4098+4107-4112
color brown, smallFCs0
show sticks, smallFCs0
show cartoon, smallFCs0
cartoon tube, smallFCs0



select RC, FlexClustObj and id 1-1781
color blue, RC
show lines, RC


select dangle, FlexClustObj and id 1782-3892
color white, dangle
show lines, dangle


select HPHOB3, FlexClustObj and resn "XXX" 
show spheres, HPHOB3
set sphere_scale=0.4
deselect HPHOB3
