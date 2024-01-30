import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class main extends Application{
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        // Create buttons for different features
        Button monitorButton = new Button("Monitor System");
        Button alertsButton = new Button("View Alerts");
        Button settingsButton = new Button("Settings");

        // Set actions for the buttons (you need to implement the actual actions)
        monitorButton.setOnAction(e -> handleMonitorButtonClick());
        alertsButton.setOnAction(e -> handleAlertsButtonClick());
        settingsButton.setOnAction(e -> handleSettingsButtonClick());

        // Create a vertical layout
        VBox layout = new VBox(10);
        layout.getChildren().addAll(monitorButton, alertsButton, settingsButton);

        // Create a scene
        Scene scene = new Scene(layout, 300, 200);

        // Set up the stage
        primaryStage.setTitle("IDS Home Screen");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    // Implement the actions for each button
    private void handleMonitorButtonClick() {
        // Add code for monitoring system
        System.out.println("Monitoring system...");
    }

    private void handleAlertsButtonClick() {
        // Add code for viewing alerts
        System.out.println("Viewing alerts...");
    }

    private void handleSettingsButtonClick() {
        // Add code for handling settings
        System.out.println("Opening settings...");
    }
}
