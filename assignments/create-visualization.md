# Project 1: Create a Visualization

**Complete by: Tuesday 27 Feb. by 12:50pm**

Now that you've learned some of the principles and techniques behind network visualization, you'll create your own visualization. You'll complete the following two items:

1. Two original visualizations of one of the social network data examples listed below. You can make any kind of network visualization you want, so long as you meet the outlined criteria. You should have one static and one dynamic visualization, using any of the tools we worked with in class. Think carefully about the different advantages of these two approaches to visualization!
2. Both visualizations should be clearly labeled, with titles and relevant information. In your static visualization, this may involve adding captions to an exported image. In your dynamic visualization, this may involve adding labels to a plot and writing in markdown cells.
3. A 2-3 paragraph written explanation of the choices you made in your visualizations and the network principles you followed. You might look back at [Ch. 4 of *The Network Turn*](https://www.cambridge.org/core/elements/network-turn/CC38F2EA9F51A6D1AFCB7E005218BBE5) to remind yourself of some of the key principles.

You'll be graded on the following criteria:

- Completeness: Both elements of the assignment are fully finished by the deadline.
- Coherence: The visual and written portions are clear and readable. The visualization makes sense without the explanation, and vice versa.
- Uniqueness: Many of the example datasets (below) are classic sample networks. You are free to search for visualizations of these online, and you will find many variations. Your visualization should include something *new* that distinguishes it from other examples.
- Argument: The uniqueness of your visualization should be in service of a particular argument or idea you are trying to get across. You may want to emphasize a certain metric or another feature of your network; you might want to call the viewer's attention to a particular node or edge. Your explanation should discuss this argument/idea and how you accomplished it in your visualization.
- Specificity: Be as specific as possible about the choices you made and why you made them. Use the explanation to walk us through your process for creating this visualization.

Choose from one of the following sample social network datasets:

- Donald Knuth's *Les Miserables* network: [lesmis.gml](/CIS397-networks/data/lesmis.gml)
- Wayne Zachary's Karate Club network: [karate.gml](/CIS397-networks/data/karate.gml)
- Adamic and Glance's political blogs network: [polblogs.gml](/CIS397-networks/data/polblogs.gml)
- Watts and Strogatz's power grid network: [power.gml](/CIS397-networks/data/power.gml)

All of these datasets are in GML format, which is compatible with most of the software we learned about. If you're using a tool (i.e. Observable) that doesn't work well with GML, remember that you can load the data in NetworkX and [export it in many different formats](https://networkx.org/documentation/stable/reference/readwrite/index.html).

[All data downloaded from [M.E.J. Newman's network data site](http://www-personal.umich.edu/~mejn/netdata/). Make sure you refer to the site for more details about your chosen data.]

---

**Requirements**:

- Turn in your assignment via Sakai.
- For your written explanation, submit a PDF that has your name, the date, your wordcount, and the citation for the dataset you used at the top. (You can find citations on Newman's website.) If your prefer, you can include the writing in your Jupyter HTML instead.
- For your static visualization, you should submit an image file on Sakai (and it may also be useful to include it in your Jupyter notebook). For your dynamic visualization, you should submit a Jupyter HTML export or another file with your visualization in it. It is your responsibility to make sure that your network is complete and viewable by the deadline.
- Explanation should be 2-3 paragraphs, about 300-400 words.