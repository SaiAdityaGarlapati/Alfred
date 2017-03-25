package com.alfred.API.Alarms;

import android.app.Activity;
import android.content.Context;

import java.util.Calendar;


/**
 * Created by manav on 25/3/17.
 */

public class AlarmsHandler {
    private Context context;
    private Activity activity;
    private Calendar time;
    private AlarmsCallback callback;
    private boolean isAlarmSet;

    public AlarmsHandler(Context context, Activity activity, Calendar time, AlarmsCallback callback) {
        this.context = context;
        this.activity = activity;
        this.time = time;
        this.callback = callback;

        setAlarm();
    }

    private void setAlarm() {

    }

    void registerCallback(AlarmsCallback callback) {
        callback.setAlarmResult(isAlarmSet);
    }

}
