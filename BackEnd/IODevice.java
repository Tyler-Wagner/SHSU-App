package BackEnd;

public class IODevice {
    private String name;
    private String type;
    private boolean status;

    public IODevice (String name, String Type)
    {
        this.name = name;
        this.type = type;
        this.status = false;
    }

    // getter methods for properties
    public String getName()
    {
        return name;
    }

    public String getType()
    {
        return type;
    }

    public Boolean getStatus()
    {
        return status;
    }

    public void setStatus(boolean status)
    {
        this.status = status;
    }
}


