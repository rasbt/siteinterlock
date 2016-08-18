delete RigidClustObj
delete RC*
delete smallRC*
delete FC*
delete HPHOB2
load 1com_nolig_flex_0001.pdb, RigidClustObj


select RC1, RigidClustObj and id 207-1708
color cyan, RC1
cartoon automatic, RC1
show cartoon, RC1

select RC2, RigidClustObj and id 169-206
color green, RC2
cartoon automatic, RC2
show cartoon, RC2

select RC3, RigidClustObj and id 133-168
color yellow, RC3
cartoon automatic, RC3
show cartoon, RC3

select RC5, RigidClustObj and id 118-126
color purpleblue, RC5
cartoon automatic, RC5
show cartoon, RC5

select smallRCs0, RigidClustObj and id 127-132+112-117+106-111+102-105+98-101+94-97+90-93+86-89+82-85+78-81+73-77+68-72+63-67+63-62+63-62+63-62+63-62+63-62+63-62+63-62+63-62+63-62+63-62+63-62+63-62+63-62+63-62+63-62+63-62+63-62+63-62+61-62+59-60+57-58+57-56+57-56+57-56+57-56+57-56+57-56+55-56+53-54+51-52+51-50+51-50
color brown, smallRCs0
show sticks, smallRCs0

select smallRCs1, RigidClustObj and id 51-50+51-50+49-50+47-48+45-46+45-44+45-44+43-44+43-42+43-42+43-42+43-42+43-42+43-42+43-42+39-42+39-38+37-38+35-36+31-34+29-30+29-28+27-28+27-26+27-26+27-26+25-26+23-24+23-22+23-22+23-22+23-22+23-22+23-22+23-22+23-22+21-22+19-20+17-18+15-16+13-14+13-12+11-12+9-10+7-8+7-6+5-6+3-4+3-2+1-2
color brown, smallRCs1
show sticks, smallRCs1



select FC, RigidClustObj and id 1709-4251
color white, FC
show lines, FC

select HPHOB2, RigidClustObj and resn "XXX" 
show spheres, HPHOB2
set sphere_scale=0.4
deselect HPHOB2
