import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

/**
 * A JUnit test class for the Person class
 */
public class PersonTest {
 
  private Person john;
  private Person sally;
 
  @Before
  public void setUp() {
    this.john = new Person("John", "Doe", 1945);
    this.sally = new Person("Sally", "Ride", 1951);
  }
 
  @Test
  public void testFirst() {
    assertEquals("John", this.john.getFirstName());
    assertEquals("Sally", this.sally.getFirstName());
  }
 
  @Test
  public void testAge() {
    assertEquals(75, this.john.getAge());
    assertEquals(69, this.sally.getAge());
  }
 
  @Test
  public void testFullName() {
    assertEquals("John Doe", this.john.getFullName());
    assertEquals("Sally Ride", this.sally.getFullName());
  }
}