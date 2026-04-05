import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int tc = Integer.parseInt(br.readLine());

        // 북 동 남 서
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};

        while (tc-- > 0) {
            String commands = br.readLine();
            int curX = 0, curY = 0;
            int dir = 0;

            int minX = 0, minY = 0, maxX = 0, maxY = 0;

            for (int i=0; i<commands.length(); i++) {
                char cmd = commands.charAt(i);

                switch (cmd) {
                    case 'F':
                        curX += dx[dir];
                        curY += dy[dir];
                        break;
                    case 'B':
                        curX -= dx[dir];
                        curY -= dy[dir];
                        break;
                    case 'L':
                        dir = (dir + 3) % 4;
                        break;
                    case 'R':
                        dir = (dir + 1) % 4;
                        break;
                }

                if (curX < minX) minX = curX;
                else if (curX > maxX) maxX = curX;
                if (curY < minY) minY = curY;
                else if (curY > maxY) maxY = curY;
            }
            int width = maxX - minX;
            int height = maxY - minY;
            sb.append(width * height).append("\n");
        }
        System.out.print(sb);
         
    }
}