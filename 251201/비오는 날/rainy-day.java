import java.util.Scanner;
class WeatherP {
    String date, day, weather;

    public WeatherP(String date, String day, String weather) {
        this.date = date;
        this.day = day;
        this.weather = weather;
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        WeatherP[] weathers = new WeatherP[n];

        for (int i = 0; i < n; i++) {
            String date = sc.next();
            String day = sc.next();
            String weather = sc.next();
            // Please write your code here.
            weathers[i] = new WeatherP(date, day, weather);

        }

        int idx=0;
        for (int i=0; i<n; i++) {
            if (weathers[i].weather.equals("Rain")) {
                idx = i;
                break;
            }
        }

        for (int i=0; i<n; i++) {
            if (weathers[i].weather.equals("Rain")) {
                if (weathers[idx].date.compareTo(weathers[i].date) >0) {
                    idx = i;
                }
            }
        }

        System.out.println(weathers[idx].date + " " + weathers[idx].day + " " + weathers[idx].weather);
    }
}