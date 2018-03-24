using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using HtmlAgilityPack;

namespace nuevoEjemplo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("BIENVENIDOS A ESTA PRUEBA !!!");
            Console.WriteLine("ingrese su busqueda :");
            String search = Console.ReadLine();
            var html = @"https://listado.mercadolibre.com.ar/"+search;
            Console.Write(html);
            parser_html(html);
            Console.ReadLine();
        }

        static void parser_html(string url)
        {
            HtmlWeb web = new HtmlWeb();
            var htmlDoc = web.Load(url);
            var nodes = htmlDoc.DocumentNode.SelectNodes("//*[@id='searchResults']//li[@class='results-item article grid product item-info-height-157']");
            /* var info = //*[@id='searchResults']//li//div[@class='carousel']//img
                        ////*[@id='searchResults']//li//div[@id]
             int index = 1;*/
            foreach (var item in nodes)
            {
                Console.WriteLine("*******************************************************************");
                //Console.WriteLine(item.InnerHtml);
                Console.WriteLine(item.SelectSingleNode(System.Xml.XPath.XPathExpression.Compile("//*[@id='searchResults']//li[@class='results-item article grid product item-info-height-157']//a")).InnerHtml);
                Console.WriteLine(item.SelectSingleNode(System.Xml.XPath.XPathExpression.Compile("//*[@id='searchResults']//li[@class='results-item article grid product item-info-height-157']//div/a")).InnerHtml);
                Console.WriteLine("*************************************************************************");
                /*Console.WriteLine("===========================");
                Console.WriteLine(item.SelectSingleNode("//*[@id='searchResults']//li[@class='results-item article grid product item-info-height-157']//img").InnerText);
                Console.WriteLine(item.SelectSingleNode("//*[@id='searchResults']//li[@class='results-item article grid product item-info-height-157']//a").InnerText);
                Console.WriteLine("===========================");*/
                Console.ReadLine();
            }
            Console.WriteLine(nodes.Count);
            
        }
        
        
    }
}
