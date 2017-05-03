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


	class MainClass
	{
		public static void Main (string[] args)
		{
			/*
			BaseClass bc = new BaseClass();  
			DerivedClass dc = new DerivedClass();  
			BaseClass bcdc = new DerivedClass();  

			bc.Method1();
			bc.Method2();

			dc.Method1();  
			dc.Method2();

			bcdc.Method1();  
			bcdc.Method2(); 
			bcdc.YouMustImplement();
			*/
			Console.WriteLine ("Obrigado!");


			//var matrix = GetBitMapColorMatrix ("/home/murillo/Pictures/MDEtMDEtMDAudHRm.png");
			//Console.WriteLine ("Hello World!");
		}

		public static Color[][] GetBitMapColorMatrix(string bitmapFilePath)
		{
			Bitmap b1 = new Bitmap(bitmapFilePath);

			int hight = b1.Height;
			int width = b1.Width;

			Color[][] colorMatrix = new Color[width][];
			for (int i = 0; i < width; i++)
			{
				colorMatrix[i] = new Color[hight];
				for (int j = 0; j < hight; j++)
				{
					colorMatrix[i][j] = b1.GetPixel(i, j);
				}
			}
			return colorMatrix;
		}
	}
}
