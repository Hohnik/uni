
import org.junit.*;
import static org.junit.Assert.*;

import java.util.List;
import java.util.Map;
import java.util.function.Predicate;

public class PasswordComplexityTest {

  /*@Test
  public void testValues(){
    assertEquals("Chars of PIN must match 0", "0", PasswordComplexity.PIN.getChars());
    assertEquals("Chars of SIMPLE must match aA", "aA", PasswordComplexity.SIMPLE.getChars());
    assertEquals("Chars of MEDIUM must match aA0", "aA0", PasswordComplexity.MEDIUM.getChars());
    assertEquals("Chars of COMPLEX must match aA0!", "aA0!", PasswordComplexity.COMPLEX.getChars());
    assertEquals("Chars of SUPER_COMPLEX must match aA0!", "aA0!", PasswordComplexity.SUPER_COMPLEX.getChars());

    assertEquals("Length of PIN must be 4", 4, PasswordComplexity.PIN.getLength());
    assertEquals("Length of SIMPLE must be 5", 5, PasswordComplexity.SIMPLE.getLength());
    assertEquals("Length of MEDIUM must be 8", 8, PasswordComplexity.MEDIUM.getLength());
    assertEquals("Length of COMPLEX must be 10", 10, PasswordComplexity.COMPLEX.getLength());
    assertEquals("Length of SUPER_COMPLEX must be 10", 16, PasswordComplexity.SUPER_COMPLEX.getLength());

  }*/

  /*@Test
  public void testGeneratePassword(){

    var lengths = 
      Map.of(
          PasswordComplexity.PIN, 4,
          PasswordComplexity.SIMPLE, 5,
          PasswordComplexity.MEDIUM, 8,
          PasswordComplexity.COMPLEX, 10,
          PasswordComplexity.SUPER_COMPLEX, 16);
    

    Map<PasswordComplexity, List<Predicate<Character>>> testPredicates  = Map.of(
          PasswordComplexity.PIN,
          List.<Predicate<Character>>of(c -> Character.isDigit(c)),
          PasswordComplexity.SIMPLE,
          List.<Predicate<Character>>of(c-> Character.isUpperCase(c), c->Character.isLowerCase(c)),
          PasswordComplexity.MEDIUM,
          List.<Predicate<Character>>of(c-> Character.isUpperCase(c), c->Character.isLowerCase(c), c->Character.isDigit(c)),
          PasswordComplexity.COMPLEX,
          List.<Predicate<Character>>of(c-> Character.isUpperCase(c), c->Character.isLowerCase(c), c->Character.isDigit(c), c->"!?+-;,.:".indexOf(c)!=-1),
          PasswordComplexity.SUPER_COMPLEX,
          List.<Predicate<Character>>of(c-> Character.isUpperCase(c), c->Character.isLowerCase(c), c->Character.isDigit(c), c->"!?+-;,.:".indexOf(c)!=-1)
          );

    for (int testRun = 0; testRun < 10; testRun++) {

      for (var complexity : PasswordComplexity.values()){
        String pass = complexity.generatePassword();
        assertEquals("Length of " + complexity.name() + " password must be " + lengths.get(complexity), (int)lengths.get(complexity), pass.length());

        for (int i = 0; i < pass.length(); i++){

          char c = pass.charAt(i);
          var predicates = testPredicates.get(complexity);

          assertTrue(complexity.name() + " password " + pass + " contains invalid character " +  c,
              predicates
              .stream( )
              .anyMatch( predicate -> predicate.test(c))
              );
        }
      }


    }

  }*/



}
