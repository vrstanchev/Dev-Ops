#!usr/bin/perl -w
 my @array=(1, 2,3);
for($i=0;$i<=3;$i++){
print($array[$i]);
if($array[$i]==3){last;}
}
print("Done");
