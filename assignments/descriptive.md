# Project 2: Descriptive Network Analysis

**THIS PROMPT IS FROM LAST SEMESTER AND MAY CHANGE FOR OUR CLASS.**

**Complete by: Tuesday 2 Apr. by 12:50pm**

Now that you've learned how to describe the main features of different kinds of networks, you're ready to begin asking and answering questions using network analysis. For your first major project of the semester, you'll create a Jupyter notebook report that explores a question about a network of your choice.

To choose a dataset, refer to our [Network Datasets](https://jrladd.com/networks/datasets.html) page. You may use the same dataset you used for the visualization assignment if you so choose, but keep in mind that if you are interested in a particular techinique, you'll want to choose a network that makes sense for that technique. A good example of this might be: you can't do an analysis of structural balance if your network doesn't have signed edges!

## Step 1: Ask a Question

In the first part of your report, you'll pose a question about the network data you've chosen. This will require you to say a little about where the data came from and what it shows. You'll want to frame the question for us by giving necessary background information, and you should cite your data source and give a link to the original file.

Framing a question is as important to good analysis as any of the statistics or coding. A good question is *specific* and *actionable*. It is *specific* in the sense that it gets at a particular detail about your network that relies on the network's context. It is *actionable* in the sense that it's answerable with the tools you've learned so far.

- The question "How many nodes are in this network?" is actionable but not specific. You can easily find out how many nodes there are, but why should we care about this question? What would having the number of nodes tell us?

- The question "How do ideas spread between web pages on the Internet?" is specific but not actionable. We have a network of web pages that we could examine, but we can't answer this question about the spread of ideas. (Or at least, not until we discuss information cascades in a few weeks.)


You'll want to frame a specific and actionable question, and then set about to answer it by describing, analyzing, and visualizing your network.

## Step 2: Describe and Analyze Your Network

Once you've crafted an introduction that appropriately frames a good research question, you can move on to the analysis, which will make up the bulk of your report.

Write well-documented code using NetworkX that helps you answer your research question. Plan out the steps before you start, and give some thought to how you organize your report. Generally, you will want to calculate some metric or statistic and then describe those results in writing. Remember not to rely on your reader to automatically know what you're talking about: the goal here is to both write good code and provide good written analysis.

Your analysis can focus on any combination of the topics we've discussed so far: centrality, density, strong & weak ties, triadic closure, homophily, communities, the small word, structural balance, etc. Choose the methods and approaches that best help you answer your question!

Your analysis should include one or two network visualizations that help you make your point. These can be of the whole network or just one relevant part: give some thought to how best to use visualization to further your argument. You can create your visualizations in Python, or you can use a tool like Gephi and insert static images into the Markdown cells. You might also find it helpful to break your analysis into sections using Markdown section headings.

At the end of your report, you should offer a brief conclusion that summarizes your findings and offers a tentative answer to your question. Did you find what you expected to find? What did the evidence show? Are there other things you'd like to try in future studies?

---

**Requirements**:

- An introduction and conclusion that frame your research question
- An analysis section with code, results, and complete written analysis
- At least one visualization, either made in Python or imported as an image
- Turn in your report (as an HTML Jupyter file) via Sakai
- For more on how this assignment will be graded, refer to the [Criteria for Good Reports](../course-info/criteria.md)