class MyThread implements Runnable
{
Thread t;
MyThread(String name)
{
t=new Thread(this,name);
System.out.println("Child thread:"+t);
t.start();
}
@Override
public void run()
{
try
{
for(int i=1;i<=3;i++)
{
System.out.println(t.getName()+":"+i);
Thread.sleep(500);
}
}
catch(InterruptedException e)
{
System.out.println(t.getName()+"is interrupted!");
}
System.out.println(t.getName()+"is terminated");
}
}
public class driver
{
public static void main(String[]args)
{
new MyThread("First Thread");
new MyThread("Second Thread");
new MyThread("Third Thread");
try
{
for(int i=1;i<=3;i++)
{
System.out.println("Main thread:"+i);
Thread.sleep(1000);
}
}
catch(InterruptedException e)
{
System.out.println("Main thread is interrupted!");
}
System.out.println("Main thread terminated");
}
}