import java.util.Arrays;

public class Alphabet {
    public static void main(String [] args){
        int num = 12;
        if (num < 1 || num > 26){
            System.out.println("Number must be between 1 and 26");
            return;
        }

        char[] letters = new char[num];
        for (int i = 0; i < num; i++){
            letters[i] = (char) ('A' + i);
        }

        System.out.println(Arrays.toString(letters));
    }
}
