delete FlexIndexObj
delete HPHOB1
load 1com_0057_pflex_in_flex_0001.pdb, FlexIndexObj

cmd.color( 's170', 'FlexIndexObj and b< 40.0')
cmd.color( 's170', 'FlexIndexObj and b= 40.0')
cmd.color( 's200', 'FlexIndexObj and b> 40.0 and b< 42.0')
cmd.color( 's200', 'FlexIndexObj and b= 42.0')
cmd.color('s225', 'FlexIndexObj and b> 42.0 and b < 44.0')
cmd.color('s225', 'FlexIndexObj and b= 44.0')
cmd.color('s250', 'FlexIndexObj and b> 44.0 and b < 46.0')
cmd.color('s250', 'FlexIndexObj and b= 46.0')
cmd.color('s280', 'FlexIndexObj and b> 46.0 and b < 48.0')
cmd.color('s280', 'FlexIndexObj and b= 48.0')
cmd.color('s310', 'FlexIndexObj and b> 48.0 and b < 49.0')
cmd.color('s310', 'FlexIndexObj and b= 49.0')
cmd.color('grey', 'FlexIndexObj and b> 49.0 and b < 50.0')
cmd.color('grey', 'FlexIndexObj and b= 50.0')
cmd.color('s690', 'FlexIndexObj and b> 50.0 and b < 52.0')
cmd.color('s690', 'FlexIndexObj and b= 52.0')
cmd.color('s730', 'FlexIndexObj and b> 52.0 and b < 54.0')
cmd.color('s730', 'FlexIndexObj and b= 54.0')
cmd.color('s760', 'FlexIndexObj and b> 54.0 and b < 56.0')
cmd.color('s760', 'FlexIndexObj and b= 56.0')
cmd.color('s790', 'FlexIndexObj and b> 56.0 and b < 58.0')
cmd.color('s790', 'FlexIndexObj and b= 58.0')
cmd.color('s820', 'FlexIndexObj and b> 58 and b < 60.0')


cmd.color('s820', 'FlexIndexObj and b= 60.0')
cmd.color('s850', 'FlexIndexObj and b> 60.0')


select HPHOB1, FlexIndexObj and resn "XXX" 
show spheres, HPHOB1
set sphere_scale=0.4
deselect HPHOB1
