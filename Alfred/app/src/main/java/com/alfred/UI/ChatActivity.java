package com.alfred.UI;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.os.Bundle;
import android.speech.RecognizerIntent;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.Toast;

import com.alfred.API.Messages.Message;
import com.alfred.API.Messages.MessageListAdapter;
import com.alfred.Constants;
import com.alfred.R;

import java.util.ArrayList;
import java.util.Locale;

public class ChatActivity extends AppCompatActivity {

    ImageButton micButton;
    ListView messageView;
    ArrayList<Message> messagesList;
    MessageListAdapter listAdapter;
    BaseClass base;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat);

        base = new BaseClass(getApplicationContext(), this);

        micButton = (ImageButton) findViewById(R.id.microphoneButton);
        messageView = (ListView) findViewById(R.id.list_view_messages);
        messagesList = new ArrayList<>();

        listAdapter = new MessageListAdapter(this, 0, messagesList);
        messageView.setAdapter(listAdapter);

        addMessages();
        listAdapter.notifyDataSetChanged();

        micButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                askForInput();
            }
        });


    }

    private void askForInput() {
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT,
                Constants.PROMPT);
        try {
            startActivityForResult(intent, Constants.REQ_CODE_SPEECH_INPUT);
        } catch (ActivityNotFoundException a) {

        }
    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case Constants.REQ_CODE_SPEECH_INPUT:
                if (resultCode == RESULT_OK && null != data) {
                    ArrayList<String> result = data
                            .getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    messagesList.add(new Message(result.get(0), true));
                    listAdapter.notifyDataSetChanged();
                }
                break;
            case Constants.REQUEST_CHECK_SETTINGS:
                Toast.makeText(this, "check settings", Toast.LENGTH_SHORT).show();

        }
    }

    private void addMessages() {
        boolean val = true;
        for (int i = 0; i < 8; i++) {
            messagesList.add(new Message("Message" + (8 - i), val));

        }
    }
}
