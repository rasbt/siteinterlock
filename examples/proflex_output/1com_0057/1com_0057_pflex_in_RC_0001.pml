delete RigidClustObj
delete RC*
delete smallRC*
delete FC*
delete HPHOB2
load 1com_0057_pflex_in_flex_0001.pdb, RigidClustObj


select RC1, RigidClustObj and id 161-1781
color cyan, RC1
cartoon automatic, RC1
show cartoon, RC1

select RC2, RigidClustObj and id 123-160
color green, RC2
cartoon automatic, RC2
show cartoon, RC2

select RC4, RigidClustObj and id 108-116
color purple, RC4
cartoon automatic, RC4
show cartoon, RC4

select smallRCs0, RigidClustObj and id 117-122+102-107+96-101+92-95+88-91+84-87+80-83+76-79+72-75+67-71+62-66+57-61+57-56+57-56+57-56+57-56+57-56+57-56+57-56+57-56+57-56+57-56+57-56+57-56+57-56+57-56+57-56+55-56+53-54+51-52+51-50+51-50+51-50+51-50+51-50+51-50+49-50+47-48+45-46+45-44+45-44+45-44+45-44+43-44+41-42+39-40
color brown, smallRCs0
show sticks, smallRCs0

select smallRCs1, RigidClustObj and id 39-38+39-38+37-38+37-36+37-36+37-36+37-36+37-36+37-36+37-36+33-36+33-32+31-32+29-30+25-28+23-24+23-22+21-22+21-20+21-20+21-20+19-20+17-18+17-16+17-16+17-16+17-16+17-16+17-16+17-16+17-16+15-16+13-14+11-12+9-10+7-8+7-6+5-6+3-4+1-2


select FC, RigidClustObj and id 1782-4299
color white, FC
show lines, FC

select HPHOB2, RigidClustObj and resn "XXX" 
show spheres, HPHOB2
set sphere_scale=0.4
deselect HPHOB2
