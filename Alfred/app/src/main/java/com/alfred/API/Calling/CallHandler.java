package com.alfred.API.Calling;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;

/**
 * Created by manav on 25/3/17.
 */

public class CallHandler {
    private Context context;
    private Activity activity;
    private CallingCallback callback;
    private int number;
    private Intent callIntent;

    public CallHandler(Context context, Activity activity, int number, CallingCallback callback) {
        this.context = context;
        this.activity = activity;
        this.number = number;
        this.callback = callback;

        generateCallIntent(number);

        registerCallingCallback(callback);
    }

    private void registerCallingCallback(CallingCallback callback) {
        callback.getCallIntent(callIntent);
    }

    private void generateCallIntent(int number) {

    }

}
