/// <summary>
/// Hilfsklasse für Array-Operationen
/// </summary>
public class ArrayHelper {
    /// <summary>
    /// Berechnet die Summe aller geraden Zahlen in einem Integer-Array
    /// </summary>
    /// <param name="numbers">Das Array mit den zu verarbeitenden Zahlen</param>
    /// <returns>Die Summe aller geraden Zahlen im Array</returns>
    public int SumEvenNumbers(int[] numbers) {
        // Initialisiere die Summe mit 0
        int sum = 0;
        
        // Durchlaufe alle Elemente des Arrays
        for (int i = 0; i < numbers.Length; i++) {
            // Prüfe, ob die aktuelle Zahl gerade ist (durch 2 teilbar)
            if(numbers[i] % 2 == 0) {
                // Addiere die gerade Zahl zur Summe hinzu
                sum += numbers[i];
            }
        }
        return sum;
    }
}