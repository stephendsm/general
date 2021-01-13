#include <stdio.h>
#include <stdlib.h>int main()

int main()
{
    /*
    float age1, age2, age3, average;
    age1 = age2 = 4.0;

    printf("Enter your age\n");
    scanf("%f", &age3);

    average = (age1 + age2 + age3) / 3;
    printf("\n The average age of the group is %f", average);
    */

    /*
    int pageView = 0;

    pageView = pageView + 1;
    printf("Page views: %d \n", pageView);

    pageView = pageView + 1;
    printf("Page views: %d \n", pageView);

    pageView = pageView + 1;
    printf("Page views: %d \n", pageView);
    */

    /*
    float balance = 1000;

    balance *= 1.1;
    printf("Balance %f \n", balance);

    balance *= 1.1;
    printf("Balance %f \n", balance);

    balance *= 1.1;
    printf("Balance %f \n", balance);
    */

    float avgProfit;
    int priceOfPumpkin = 10;
    int sales = 59;
    int daysWorked = 7;

    avgProfit = ((float)priceOfPumpkin * (float)sales) / (float)daysWorked; // temporarily changes to float (from int)

    printf("%.2f", avgProfit);



    return 0;
}
