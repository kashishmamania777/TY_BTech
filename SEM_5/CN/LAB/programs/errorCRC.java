import java.util.*;

public class errorCRC {

    public static String divide(String dividend, String divisor) {
        int len = divisor.length();
        StringBuilder remainder = new StringBuilder(dividend);

        for (int i = 0; i < dividend.length() - divisor.length() + 1; i++) {
            if (remainder.charAt(i) == '1') {
                for (int j = 0; j < len; j++) {
                    remainder.setCharAt(i + j, (remainder.charAt(i + j) == divisor.charAt(j)) ? '0' : '1');
                }
            }
        }
        return remainder.substring(remainder.length() - len + 1);
    }

    public static String crc(String dataword, String divisor) {
        String paddedWord = dataword + "0".repeat(divisor.length() - 1);
        String remainder = divide(paddedWord, divisor);
        return remainder;
    }

    public static void check(String receivedCW, String divisor) {
        String remainder = divide(receivedCW, divisor);

        if (remainder.chars().allMatch(ch -> ch == '0')) {
            System.out.println("Codeword received correctly.");
            String original = receivedCW.substring(0, receivedCW.length() - (divisor.length() - 1));
            System.out.println("Original Dataword: " + original);
        } else {
            System.out.println("Error detected in the received codeword.");
        }
    }
      public static String Errorcheck(String codeword) {
        Random random = new Random();
        char[] codewordArray = codeword.toCharArray();
        int errorIndex = random.nextInt(codewordArray.length);
        codewordArray[errorIndex] = (codewordArray[errorIndex] == '0') ? '1' : '0';
        return new String(codewordArray);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        System.out.print("Enter the dataword: ");
        String dataword = scanner.nextLine();

        System.out.print("Enter the divisor: ");
        String divisor = scanner.nextLine();

        String crc = crc(dataword, divisor);
        String codeword = dataword + crc;

        System.out.println("\nSender:");
        System.out.println("Dataword: " + dataword);
        System.out.println("Divisor: " + divisor);
        System.out.println("CRC: " + crc);
        System.out.println("Codeword: " + codeword);

        System.out.println("\nReceiver:");
        check(codeword, divisor);
        
        String receivedCodeword = Errorcheck(codeword);

        System.out.println("\nReceiver:");
        System.out.println("Received Codeword: " + receivedCodeword);
        check(receivedCodeword, divisor);
       
    }

}

