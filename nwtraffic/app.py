from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from network_traffic_analyzer import analyze_traffic  # Import the analysis function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Call the analyze_traffic function from network_traffic_analyzer
    scatter_plot, pie_chart, src_ip_bar_graph, dst_ip_bar_graph = analyze_traffic()

    # Save the results to the static folder
    scatter_plot.savefig('static/analysis.png')
    plt.close(scatter_plot)
    
    pie_chart.savefig('static/protocol_distribution.png')
    plt.close(pie_chart)
    
    src_ip_bar_graph.savefig('static/src_ip_packet_counts.png')
    plt.close(src_ip_bar_graph)
    
    dst_ip_bar_graph.savefig('static/dst_ip_packet_counts.png')
    plt.close(dst_ip_bar_graph)

    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
