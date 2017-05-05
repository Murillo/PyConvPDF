using System;
using System.Drawing;

namespace ConsoleTeste
{
	public abstract class myBase
	{
		public abstract void YouMustImplement();

		public virtual void YouCanOverride()
		{ 
			Console.WriteLine ("My Base");
		}
	}

	class BaseClass : myBase
	{  
		public override void YouMustImplement(){
			Console.WriteLine ("BaseClass - YouMustImplement");
		}

		public virtual void Method1()  
		{  
			Console.WriteLine("Base - Method1");  
		}  

		public void Method2()  
		{  
			Console.WriteLine("Base - Method2");  
		}  
	}  

	class DerivedClass : BaseClass  
	{  
		public override void Method1()  
		{  
			Console.WriteLine("Derived - Method1");  
		}  

		public new void Method2()  
		{  
			Console.WriteLine("Derived - Method2");  
		}  
	}  

	class DerivedClass : BaseClass  
	{  
		public override void Method1()  
		{  
			Console.WriteLine("Derived - Method1");  
		}  

		public new void Method2()  
		{  
			Console.WriteLine("Derived - Method2");  
		}  
	}  
}
