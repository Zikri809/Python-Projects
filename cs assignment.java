import java.util.Scanner;
import java.text.DecimalFormat;

class Test
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner (System.in);
        DecimalFormat df = new DecimalFormat ("0.00");
        
        System.out.print("\t\tStudent Performance SC025 2023/2024");
        System.out.print("\n\t\t****************************************");
        
        System.out.print("\n\t\tEnter number of students: ");
        int studnum= in.nextInt();
        
        double [] MarkList = new double [studnum];
        int i = 0;
        double sum = 0.00;
        
        while (i < MarkList.length)
        {
            System.out.print("\t\tEnter Mark  : ");
            double mark = in.nextDouble();
            //System.out.print("\n");
            if((mark > 100)||(mark < 0))
            {
                System.out.print("\t\t\tInvalid mark!\n");
            }
            else
            {
                MarkList[i] = mark;
                sum = sum + MarkList[i];
                i++;
            }
        }


        double acount = 0;
        double bcount = 0;
        double ccount = 0;
        double dcount = 0;
        double ecount = 0;
        double fcount = 0;

    
        for (int x=0;x<MarkList.length;x++) {
            if (MarkList[x]>=90) {
                acount+=1.0;
            }
            else if (MarkList[x]>=80) {
                bcount+=1.0;
            }
            else if (MarkList[x]>=70) {
                ccount+=1.0;
            }
            else if (MarkList[x]>=60) {
                dcount+=1.0;
            }
            else if (MarkList[x]>=50) {
                ecount+=1.0;
            }
            else 
            {
                fcount+=1.00;
            } 
        }

        double totalcount=acount+bcount+ccount+dcount+ecount+fcount;



        System.out.print("\n\t\tStudent Performance Analysis");
        System.out.print("\n\t\t********************************");
        System.out.print("\n\t\tThe summation of all mark is : " +df.format(sum));
        double mean = sum / totalcount;
        System.out.println("\n\t\tThe mean of all mark is : " +df.format(mean));
        
        
        double aper=(acount/totalcount)*100;
        double bper=(bcount/totalcount)*100;
        double cper=(ccount/totalcount)*100;
        double dper=(dcount/totalcount)*100;
        double eper=(ecount/totalcount)*100;
        double fper=(fcount/totalcount)*100;

        double totalper=aper+bper+cper+dper+eper+fper;



        System.out.print("\n\t\t---------------------------------------------------");
        System.out.print("\n\t\tGrade\tNumber of Students\tPercentage");
        System.out.print("\n\t\t---------------------------------------------------");
        System.out.print("\n\t\tA\t  "+acount+"\t\t\t  "+df.format(aper)+"%");
        System.out.print("\n\t\tB\t  "+bcount+"\t\t\t  "+df.format(bper)+"%");
        System.out.print("\n\t\tC\t  "+ccount+"\t\t\t  "+df.format(cper)+"%");
        System.out.print("\n\t\tD\t  "+dcount+"\t\t\t  "+df.format(dper)+"%");
        System.out.print("\n\t\tE\t  "+ecount+"\t\t\t  "+df.format(eper)+"%");
        System.out.print("\n\t\tF\t  "+fcount+"\t\t\t  "+df.format(fper)+"%");
        System.out.print("\n\t\t---------------------------------------------------");
        System.out.print("\n\t\tTotal\t  "+totalcount+"\t\t\t  "  +df.format(totalper)+"%");
        System.out.print("\n\t\t---------------------------------------------------\n");

        double highest=-999;
        double lowest=999;
        int highloc=0;
        int lowloc=0;

        for (int loccount=0;loccount<MarkList.length; loccount++){
            if (MarkList[loccount]>highest){
                highest=MarkList[loccount];
            
                highloc=loccount;
            }
            if (MarkList[loccount]<lowest){
                lowest=MarkList[loccount];
                lowloc=loccount;
            }
        }
        
        
        
        System.out.print("\n\t\tHighest & Lowest Mark");
        System.out.print("\n\t\t***************************");
        System.out.print("\n\t\tThe Highest mark is : "+df.format(highest)+". (Index Location : "+highloc+")");
        System.out.print("\n\t\tThe Highest mark is : "+df.format(lowest)+". (Index Location : "+lowloc+")");


    }
}