
import org.junit.*;
import static org.junit.Assert.*;

public class PasswordEntryTest{

  /*@Test
  public void testConstructor(){

    PasswordEntry entry = new PasswordEntry("reddit.com", "lurker123", PasswordComplexity.MEDIUM);
    assertEquals("website must be reddit.com", "reddit.com", entry.getWebsite());
    assertEquals("login must be lurker123", "lurker123", entry.getLoginName());
    assertEquals("complexity must be MEDIUM", PasswordComplexity.MEDIUM, entry.getPasswordComplexity());
    assertNotNull("password must be generated", entry.getPassword());

    assertThrows("null website is not allowed",
        IllegalArgumentException.class, () -> new PasswordEntry(null, "lurker123", PasswordComplexity.MEDIUM));
    assertThrows("blank website is not allowed",
        IllegalArgumentException.class, () -> new PasswordEntry("   ", "lurker123", PasswordComplexity.MEDIUM));
    assertThrows("password complexity must not be null",
        IllegalArgumentException.class, () -> new PasswordEntry("reddit.com", "lurker123", null));

    entry = new PasswordEntry("reddit.com", null, PasswordComplexity.MEDIUM);
    assertNull("null login name is possible", entry.getLoginName());

    entry = new PasswordEntry("reddit.com", "", PasswordComplexity.MEDIUM);
    assertEquals("empty login name is possible", "", entry.getLoginName());

  }*/

  /*@Test
  public void testConstructor2(){
    PasswordEntry entry = new PasswordEntry("reddit.com", PasswordComplexity.MEDIUM);
    assertEquals("website must be reddit.com", "reddit.com", entry.getWebsite());
    assertNull("login must be null", entry.getLoginName());
    assertEquals("complexity must be MEDIUM", PasswordComplexity.MEDIUM, entry.getPasswordComplexity());
    assertNotNull("password must be generated", entry.getPassword());

    assertThrows("null website is not allowed",
        IllegalArgumentException.class, () -> new PasswordEntry(null, PasswordComplexity.MEDIUM));
    assertThrows("blank website is not allowed",
        IllegalArgumentException.class, () -> new PasswordEntry("   ", PasswordComplexity.MEDIUM));
    assertThrows("password complexity must not be null",
        IllegalArgumentException.class, () -> new PasswordEntry("reddit.com", null));
  }*/

  /*@Test
  public void testCopyConstructor(){
    PasswordEntry entry = new PasswordEntry("reddit.com", "lurker123", PasswordComplexity.MEDIUM);
    PasswordEntry anotherEntry = new PasswordEntry("reddit.com", "lurker123", PasswordComplexity.MEDIUM);
    entry.setNextEntry(anotherEntry);
    PasswordEntry copy = new PasswordEntry(entry);
    assertEquals("website of clone must be reddit.com", "reddit.com", copy.getWebsite());
    assertEquals("login of clone must be lurker123", "lurker123", copy.getLoginName());
    assertEquals("password of clone must be 12345", entry.getPassword(), copy.getPassword());
    assertSame("next entry of copy must be the same as next entry of original entry",
        anotherEntry, copy.getNextEntry());

    assertThrows("other must not be null",
        IllegalArgumentException.class,
        () -> new PasswordEntry(null));

  }*/

  /*@Test
  public void testRegeneratePassword(){
    PasswordEntry entry = new PasswordEntry("reddit.com", "lurker123", PasswordComplexity.MEDIUM);

    String password = entry.getPassword();

    entry.regeneratePassword();

    assertNotSame("generate password must generate a new password", 
        password, entry.getPassword());

  }*/

  /*@Test
  public void testEquals(){

    PasswordEntry entry = new PasswordEntry("reddit.com", "lurker123", PasswordComplexity.MEDIUM);

    assertTrue("identical entries must be equal", entry.equals(entry));
    assertFalse("null is not equal", entry.equals(null));
    assertFalse("String is a different type", entry.equals("Entry!"));

    assertFalse("entries with different websites are not equal ",
        entry.equals(new PasswordEntry("gitlab.com", "lurker123", PasswordComplexity.MEDIUM)));

    assertFalse("entries with different login names are not equal ",
        entry.equals(new PasswordEntry("reddit.com", "cow123", PasswordComplexity.MEDIUM)));

    assertTrue("entries with different password complexities are not equal",
        entry.equals(new PasswordEntry("reddit.com", "lurker123", PasswordComplexity.MEDIUM)));

    PasswordEntry other = new PasswordEntry("reddit.com", "lurker123", PasswordComplexity.MEDIUM);
    other.setNextEntry(new PasswordEntry("a", "b", PasswordComplexity.MEDIUM));
    assertTrue("entries with different next entries are equal ",
        entry.equals(other));

    assertTrue("equal must return true for equal entries",
        entry.equals(new PasswordEntry("reddit.com", "lurker123", PasswordComplexity.MEDIUM)));

  }*/

}
