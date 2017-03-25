package com.alfred.UI;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.location.Location;
import android.widget.Toast;

import com.alfred.API.Alarms.AlarmsCallback;
import com.alfred.API.Alarms.AlarmsHandler;
import com.alfred.API.Calling.CallHandler;
import com.alfred.API.Calling.CallingCallback;
import com.alfred.API.Contacts.ContactCallback;
import com.alfred.API.Contacts.ContactHandler;
import com.alfred.API.Contacts.ContactImpl;
import com.alfred.API.Directions.DirectionsCallback;
import com.alfred.API.Directions.DirectionsHandler;
import com.alfred.API.Location.LocationCallback;
import com.alfred.API.Location.LocationHandler;

import java.util.Calendar;

/**
 * Created by manav on 23/3/17.
 */

public class BaseClass implements LocationCallback, DirectionsCallback, AlarmsCallback, ContactCallback, CallingCallback {
    private Context context;
    private Activity activity;
    private String address;
    private String destination;
    private Location location;

    public BaseClass(Context context, Activity activity) {
        this.context = context;
        this.activity = activity;
    }

    void getLocation() {
        new LocationHandler(context, activity, this);
    }

    void getDirections(String destination) {
        new DirectionsHandler(context, activity, destination, this);
    }

    void setAlarm() {
        new AlarmsHandler(context, activity, Calendar.getInstance(), this);
    }

    void makeCall() {
        new CallHandler(context, activity, 0, this);
    }

    void saveContact() {
        new ContactHandler(context, activity, this);
    }


    @Override
    public void updateLocation(Location location) {
        this.location = location;
    }

    @Override
    public void updateAddress(String address) {
        Toast.makeText(context, address, Toast.LENGTH_SHORT).show();
    }

    @Override
    public void sendDirectionsIntent(Intent intent) {
        activity.startActivity(intent);
    }

    @Override
    public void setAlarmResult(boolean value) {

    }

    @Override
    public void getCallIntent(Intent intent) {

        activity.startActivity(intent);
    }

    @Override
    public void getContact(ContactImpl contact) {

    }

    @Override
    public void contactSaveStatus(boolean saved) {

    }
}
