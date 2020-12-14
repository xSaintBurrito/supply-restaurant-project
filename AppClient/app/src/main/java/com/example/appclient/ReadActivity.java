package com.example.appclient;

import androidx.appcompat.app.AppCompatActivity;


import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;



public class ReadActivity extends AppCompatActivity {

    TextView table;
    String chain;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_read);

        table = (TextView) findViewById(R.id.readTable);


        myJsonRquest();

    }
public void myJsonRquest() {
    RequestQueue queue = Volley.newRequestQueue(this);
    String url = "http://192.168.137.1:5000";
    JsonObjectRequest requestJson = new JsonObjectRequest(Request.Method.GET, url, null, new Response.Listener<JSONObject>() {
        @Override
        public void onResponse(JSONObject response) {

            table.setText(response.toString());
        }
    }, new Response.ErrorListener() {
        @Override
        public void onErrorResponse(VolleyError error) {
            table.setText(error.toString());
        }
    });
    queue.add(requestJson);
    }
}






