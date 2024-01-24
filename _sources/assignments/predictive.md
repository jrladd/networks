# Project 3: Predictive Network Analysis

**THIS PROMPT IS FROM LAST SEMESTER AND MAY CHANGE FOR OUR CLASS.**

**Complete by: Tuesday 11 May by 2pm**

You've now learned a much wider array of techniques for working with networks, and it's time to apply those in a second big project.  This second project will follow the same form as the first: you'll create a Jupyter notebook report that explores a question about a network of your choice.

To choose a dataset, refer to our [Network Datasets](../resources/datasets.md) page. You may use the same dataset you used for either of the previous assignments if you so choose, but keep in mind that if you are interested in a particular techinique, you'll want to choose a network that makes sense for that technique. A good example of this might be: you can't do an analysis of structural balance if your network doesn't have signed edges!

**On Tuesday 25 April (by our class time, 12:50pm), you'll turn in a one-page proposal that suggests a dataset and gives a possible research question, with a paragraph or two explaining the steps you plan to take. This will allow us to meet and discuss your project over the next few weeks.**

## Step 1: Ask a Question

In the first part of your report, you'll pose a question about the network data you've chosen. This will require you to say a little about where the data came from and what it shows. You'll want to frame the question for us by giving necessary background information, and you should cite your data source and give a link to the original file.

Framing a question is as important to good analysis as any of the statistics or coding. Like last time, you'll want your question to be *specific* and *actionable*. In particular, make sure your question relates to the data set that you are working on. You can ask "What is the most important node?" of any network, but why would you want to know that about *your* network?

**This time, you'll ask a question that will allow you to do the more advanced kinds of analysis that we've been discussing in the last few weeks of class.You'll want to frame a specific and actionable question, and then set about to answer it by describing, analyzing, and visualizing your network.**

## Step 2: Describe Your Network

Once you've crafted an introduction that appropriately frames a good research question, you can move on to describing your network and beginning to answer your research question. This section will be similar to section two from last time, with both code and written analysis. Use all the descriptive tools at your disposal to try to answer your question, before moving on to the more complex analysis steps in the next section.

Your analysis should include one or two network visualizations that help you make your point. These can be of the whole network or just one relevant part: give some thought to how best to use visualization to further your argument. You can create your visualizations in Python, or you can use a tool like Gephi and insert static images into the Markdown cells. You might also find it helpful to break your analysis into sections using Markdown section headings.

## Step 3: Analyze Your Network

This final section will make up the bulk of your report. Write well-documented code using NetworkX that helps you answer your research question. Plan out the steps before you start, and give some thought to how you organize your report. Generally, you will want to calculate some metric or statistic and then describe those results in writing. Remember not to rely on your reader to automatically know what you're talking about: the goal here is to both write good code and provide good written analysis.

Your analysis can focus on any combination of the advanced topics we've discussed in class: multilayer networks, information cascades, epidemics, citation analysis, modeling, etc. Choose the methods and approaches that best help you answer your question!

This section should include a few additional data visualizations---these can be network visualizations, or they may be charts and graphs that illuminate network metrics. Make sure all visualizations are explained completely, accurately, and in terms of the data.

At the end of your report, you should offer a brief conclusion that summarizes your findings and offers a tentative answer to your question. Did you find what you expected to find? What did the evidence show? Are there other things you'd like to try in future studies?

---

**Requirements**:

- An introduction and conclusion that frame your research question
- Two analysis sections (i.e. description and analysis) with code, results, and complete written analysis
- Several visualizations in both the description and analysis sections, either made in Python or imported as images
- Turn in your report (as an HTML file) via Sakai
- For more on how this assignment will be graded, refer to the [Criteria for Good Reports](../resources/criteria.md)