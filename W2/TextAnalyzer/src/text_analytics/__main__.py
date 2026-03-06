from .analyzer import TextAnalyzer
from .reports import generate_text_report, generate_word_cloud_data, generate_frequency_table
import sys

def main():
    """Main entry point for the text analyzer."""
    # Parse command line arguments
    # Load text file
    # Run analysis
    # Generate reports
    wfn = 10
    exclude_stop = True
    bgn = 5
    tgn = 5
    for i, arg in enumerate(sys.argv[1:]):
        match i:
            case 0:
                wfn = int(arg)
            case 1:
                exclude_stop = arg.lower() == 'true'
            case 2:
                bgn = int(arg)
            case 3:
                tgn = int(arg)
        


    input_file = "../samples/sam-i-am.txt" # put green eggs & ham in here
    # load text file
    with open(input_file, 'r') as f:
        text: str = f.read()

    # run analysis
    analyzer = TextAnalyzer(text)
    result = analyzer.analyze(wfn, exclude_stop, bgn, tgn)

    # generate reports
    print("Running text report...")
    generate_text_report(result, "../output/report.txt")

    wf: list = analyzer.get_word_frequencies()
    # print(f"Word Cloud Data: \n{generate_word_cloud_data(wf)}")
    # print(f"Frequency Table: \n{generate_frequency_table(wf)}")


if __name__ == "__main__":
    main()