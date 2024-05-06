<?php
session_start();
$appliances=$_GET['app'];
$con=mysqli_connect("localhost","cshubnet_home","home123","cshubnet_home");
$sql="";
if($appliances=="1")
{
		$sql="select * from status where id=1";
		$result=mysqli_query($con,$sql);
		$row=mysqli_fetch_assoc($result);
		$res=$row['app1'];
		if($res=="0")
		{
		$sql="update status set app1=1 where id=1";
		$result=mysqli_query($con,$sql);
		}
		else
		{
		$sql="update status set app1=0 where id=1";
		$result=mysqli_query($con,$sql);
		}
}
else if($appliances=="2")
{
		$sql="select * from status where id=1";
		$result=mysqli_query($con,$sql);
		$row=mysqli_fetch_assoc($result);
		$res=$row['app2'];
		if($res=="0")
		{
		$sql="update status set app2=1 where id=1";
		$result=mysqli_query($con,$sql);
		}
		else
		{
		$sql="update status set app2=0 where id=1";
		$result=mysqli_query($con,$sql);
		}
}
else if($appliances=="3")
{
		$sql="select * from status where id=1";
		$result=mysqli_query($con,$sql);
		$row=mysqli_fetch_assoc($result);
		$res=$row['app3'];
		if($res=="0")
		{
		$sql="update status set app3=1 where id=1";
		$result=mysqli_query($con,$sql);
		}
		else
		{
		$sql="update status set app3=0 where id=1";
		$result=mysqli_query($con,$sql);
		}
}
else if($appliances=="4")
{
		$sql="select * from status where id=1";
		$result=mysqli_query($con,$sql);
		$row=mysqli_fetch_assoc($result);
		$res=$row['app4'];
		if($res=="0")
		{
		$sql="update status set app4=1 where id=1";
		$result=mysqli_query($con,$sql);
		}
		else
		{
		$sql="update status set app4=0 where id=1";
		$result=mysqli_query($con,$sql);
		}
}
echo '<?xml version="1.0"?>';
echo '<login>';
echo '<status>SUCCESS</status>';
echo '<message>Done</message>';
echo '<sid>'.SID.'</sid>';
echo '</login>';
?>