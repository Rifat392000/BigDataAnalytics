import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MapForWordCount extends Mapper<LongWritable, Text, Text, IntWritable> { @Override
	  public void map(LongWritable key, Text value, Context context)
		      throws IOException, InterruptedException {

		    String line = value.toString();
		    String[] words = line.split(",");
		    for(int i=0;i<words.length-1;i++){
		    	for(int j=i+1;j<words.length;j++){
		    		if((words[i].charAt(0))<(words[j].charAt(0))){
		    			context.write(new Text(words[i]+", "+words[j]),new IntWritable(1));
		    		}
		    		else{
		    			context.write(new Text(words[j]+", "+words[i]),new IntWritable(1));
		    		}
		    		
		    	}
		    	
		    }

		  }}
