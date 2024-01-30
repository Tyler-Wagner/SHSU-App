package FrontEnd;

//JavaFX imports
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ScrollPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

//pcap4j imports
import org.pcap4j.core.PcapNetworkInterface;
import org.pcap4j.core.Pcaps;

//java imports
import java.util.List;


public class main extends Application{
    public static void main(String[] args){
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {

        //create a VBox to hold all of the buttons
        VBox vbox = new VBox();
        vbox.setSpacing(10);

        //get all of the packet capture options
        try
        {
            List<PcapNetworkInterface> captureOptions = Pcaps.findAllDevs();

            //create all of the buttons that are in the list
            for(PcapNetworkInterface networkInterface : captureOptions)
            {
                String interfaceName = networkInterface.getName();
                Button button = new Button(interfaceName);

                //setting up an event handler for button clicks
                button.setOnAction(event -> handleButtonClick(interfaceName));

                vbox.getChildren().add(button);
            }
        }
        catch(Exception e)
        {
            System.err.println("Errored with exception: " + e.getMessage());
        }

        //use a scroll pane to handle cases where buttons exceed the visable area
        ScrollPane scrollPane = new ScrollPane(vbox);

        //set up the scene with the scroll pane
        Scene scene = new Scene(scrollPane, 400, 300);
        primaryStage.setScene(scene);

               
        //set up the stage (screen)
        primaryStage.setTitle("Packet Capture Options");

        //show the stage
        primaryStage.show();
    }

    //event handler for button clicks
    private void handleButtonClick(String interfaceName)
    {
        System.out.println("Button clicked for interface: " + interfaceName);
        //logic to go to the main screen will go here after.
    }

}
