using System;
using Emgu.CV;


/*
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");
*/


namespace myNamespace
{
    class Test
    {
        static void Main(string[] args)
        {
            Mat pic = new Mat(); 
            pic = CvInvoke.Imread("./1182.jpg"); 
            /*
            Mat gaussianBlur = new Mat(); 
            CvInvoke.GaussianBlur(pic, gaussianBlur, new System.Drawing.Size(3, 3), 7.0); 
            CvInvoke.Imshow("starry night", pic);
            */
            CvInvoke.Imshow("picture", pic); 
            CvInvoke.WaitKey(); 
        }
    }
}

/*
app.Run();
*/