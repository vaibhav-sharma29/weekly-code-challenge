import java.util.Scanner;

public class Main {
    public static int getStartStation(int[] charge, int[] cost) {
        int total = 0, current = 0, start = 0;
        if (charge.length == 0) return -1;
        
        for (int i = 0; i < charge.length; i++) {
            int diff = charge[i] - cost[i];
            total += diff;
            current += diff;
            
            if (current < 0) {
                start = i + 1;
                current = 0;
            }
        }
        return total >= 0 ? start : -1;
    }

    public static int[] parseLine(String line) {
        String cleaned = line.replaceAll("[^0-9]+", " ").trim();
        if (cleaned.isEmpty()) return new int[0];
        
        String[] parts = cleaned.split("\\s+");
        int[] arr = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            arr[i] = Integer.parseInt(parts[i]);
        }
        return arr;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line1 = sc.nextLine();
            String line2 = sc.nextLine();
            
            int[] charge = parseLine(line1);
            int[] cost = parseLine(line2);
            
            System.out.println(getStartStation(charge, cost));
        }
        sc.close();
    }
}