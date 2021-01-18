/**
 * 
 */
package application;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;

/**
 * @author profi
 *
 */
public class MainController {
	@FXML
	private Label MPH;
	@FXML
	private Label RPM;
	@FXML
	private Label odm;
	@FXML
	private Label b36;
	@FXML
	private Label b35;
	@FXML
	private Label b34;
	@FXML
	private Label b33;
	@FXML
	private Label b32;
	@FXML
	private Label b31;
	
	int i = 0;
	@FXML
	public void feedData(ActionEvent action) {
		
		String s =String.valueOf(i);
		String b = String.valueOf(100 - i);
		String o = String.valueOf(1000 + i);
		MPH.setText(s);
		RPM.setText(s);
		odm.setText(o);
		b36.setText(b+"%");
		b35.setText(b+"%");
		b34.setText(b+"%");
	    b33.setText(b+"%");
		b32.setText(b+"%");
		b31.setText(b+"%");
		
		i++;
	}
	
}
