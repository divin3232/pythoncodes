public class Question5 {
    
	public static void main(String[] args) {
        String name = "Feel the mood";
        char letterCheck = 'F';
        
        int count = occur(name,  letterCheck);
        System.out.println("The letter '" +  letterCheck + "' appears " + count + " times.");
    }

    public static int occur(String name, char  letterCheck) {
        int kind = 0;
        for (int i = 0; i < name.length(); i++) {
            if (name.charAt(i) ==  letterCheck) {
                kind++;
            }
        }
        return kind;
    }
}
