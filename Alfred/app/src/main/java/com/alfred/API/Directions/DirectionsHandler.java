package com.alfred.API.Directions;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;

/**
 * Created by manav on 22/3/17.
 */

public class DirectionsHandler {
    private Context context;
    private Activity activity;
    private String destination;
    private DirectionsCallback callback;

    public DirectionsHandler(Context context, Activity activity, String destination, DirectionsCallback callback) {
        this.context = context;
        this.activity = activity;
        this.destination = destination;
        registerDirectionsCallBack(callback);
    }

    private void registerDirectionsCallBack(DirectionsCallback callback) {
        Uri uri = Uri.parse("google.navigation:q=Taj+Mahal,+Agra");
        Intent mapIntent = new Intent(Intent.ACTION_VIEW, uri);
        mapIntent.setPackage("com.google.android.apps.maps");
        callback.sendDirectionsIntent(mapIntent);
    }
}
