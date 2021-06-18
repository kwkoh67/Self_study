//Basketball.java


class Point
{
	private int total = 0;
	synchronized void goalin(int point){
		total = total + point;
	}
	int gettotal()
	{
		return total;
	}

}

class Player extends Thread
{
	Point goal;
	Player (Point number) 
	{
		goal = number; 
	}

	public void run(){

		try{
			for (int n = 0 ; n < 100 ;n++ )
			{
				int pt = (int)(Math.random()*10)%3+1;
				goal.goalin(pt);
				System.out.println("¼±¼ö("+getName()+")"+pt+"Á¡");
				
				int sleep_time = (int)(Math.random()*10);
				sleep(sleep_time);
				if(goal.gettotal()>=20) break;
			}


		}
		catch(Exception e)
		{
			System.out.println(e);
		}

	}
}

class Basketball
{

	
	


}