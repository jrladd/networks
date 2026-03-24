# Project 3: Predictive Network Analysis

**Complete by: Sunday 3 May at 5pm**

You've now learned a much wider array of techniques for working with networks dynamically, and it's time to apply those in a third big project.  This third project will combine the forms of the first and second: you'll create visualizations, code, and a Jupyter notebook report that explores a question about a network of your choice.

**You may work on your own or with a partner on this project. If you choose to work as a pair, each of you will turn in an additional self-assessment document outlining your role in the project. I will distribute this document after the proposals are complete. You may not work in groups larger than two.**

## Project Proposal: Thursday 2 Apr.

On Thursday 2 April (by our class time), you'll turn in a one- to two-page proposal that includes the following:

- a short explanation of the dataset you intend to use, with a link and citation to the data
- a paragraph detailing your research question(s) (see the [Project 2 Prompt](descriptive.md) for guidelines on asking good questions)
- a paragraph detailing the methods and approaches you intend to use, both descriptive and predictive (see below for more)
- a timeline of how you intend to use each of the four weeks from the proposal to the final deadline
- a short annotated bibliography with at least three sources pertaining to the data and/or methods you intend to use.

To choose a dataset, refer to our [Network Datasets](../resources/datasets.md) page. You may use the same dataset you used for either of the previous assignments if you so choose, but keep in mind that if you are interested in a particular techinique, you'll want to choose a network that makes sense for that technique. A good example of this might be: you can't do an analysis of structural balance if your network doesn't have signed edges!

## Presentation Materials: Thursday 23 Apr.

This is detailed further on the [Presentation prompt](presentation.md). On the last day of class you will turn in the materials you intend to share for the presentation. Your project does not need to be fully complete at this point, but you should have enough done to be able to present it in a compelling way.

## Final Report: Sunday 3 May at 5pm

Your report should have the following sections.

### Introduction

In the first part of your report, you'll pose a question about the network data you've chosen. This will require you to say a little about where the data came from and what it shows. You'll want to frame the question for us by giving necessary background information, and you should cite your data source and give a link to the original file.

Framing a question is as important to good analysis as any of the statistics or coding. Like last time, you'll want your question to be *specific* and *actionable*. In particular, make sure your question relates to the data set that you are working on. You can ask "What is the most important node?" of any network, but why would you want to know that about *your* network?

**This time, you'll ask a question that will allow you to perform dynamic or predictive analysis, as we've been discussing in the last few weeks of class. You'll want to frame a specific and actionable question, and then set about to answer it by describing, analyzing, and visualizing your network.**

### Descriptive Analysis

Once you've crafted an introduction that appropriately frames a good research question, you can move on to describing your network and beginning to answer your research question. This section will be similar to section two from last time, with both code and written analysis. Use all the descriptive tools at your disposal to begin to answer your question, before moving on to the more complex analysis steps in the next section.

Your analysis should include one or two network visualizations that help you make your point. These can be of the whole network or just one relevant part: give some thought to how best to use visualization to further your argument. You can create your visualizations in Python, or you can use a tool like Gephi and insert static images into the Markdown cells. You might also find it helpful to break your analysis into sections using Markdown section headings.

### Predictive/Dynamic Analysis

This final section will make up the bulk of your report. Write well-documented code using NetworkX that helps you answer your research question. Plan out the steps before you start, and give some thought to how you organize your report. Remember not to rely on your reader to automatically know what you're talking about: the goal here is to both write good code and provide good written analysis.

Your analysis can focus on any combination of the advanced topics we've discussed in class: multipartite or multilayer networks, information cascades, epidemics, citation analysis, modeling, etc. Choose the methods and approaches that best help you answer your question! *You are encouraged to seek out new methods and extend the existing ones we've learned about in class.* I am happy to review and discuss methods as you work.

This section should include data visualizations of various kinds---these can be network visualizations and/or charts and graphs that illuminate network metrics. Make sure all visualizations are explained completely, accurately, and in terms of the data.

### Conclusion

At the end of your report, you should offer a conclusion that summarizes your findings and offers a tentative answer to your question. Did you find what you expected to find? What did the evidence show? Are there other things you'd like to try in future studies?

### Bibliography

This is a short bibliography with at least 5 sources and a sentence or two about how each was used. You can include the sources you used for your proposal, but you should have at least 2 new ones.

---

**Requirements**:

- An introduction and conclusion that frame your research question
- Two body sections (i.e. description and analysis) with code, results, and complete written analysis
- Several visualizations in both the description and analysis sections, either made in Python or imported as images
- A bibliography of at least 5 sources
- Turn in your report via Github Classroom
- For more on how this assignment will be graded, refer to the [Criteria for Good Reports](../course-info/criteria.md)