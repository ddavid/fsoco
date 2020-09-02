# FSOCO
<small>Formula Student Objects in Context</small>

## Deprecation Notice 06.08.2020
This project will not be actively maintained anymore.

The [second iteration of the FSOCO dataset](https://github.com/fsoco/fsoco-dataset/) has completed beta testing and is awaiting your contribution.
Check out the new [website](https://www.fsoco-dataset.com).

This second iteration does **not** contain the data from the first one from the start, but migration of your datasets is possible, if you fulfill the new requirements - for most only small changes will be needed to achieve this.
You can read into [the reasoning behind this break](https://www.fsoco-dataset.com/overview/#differences-to-fsocov1) between the first and second iteration.

![FSD pylon mosaic](https://imgur.com/JMCV3Dr.png)

## Contributing
We have set a minimum contribution amount of <strong>600</strong> images.<br/>
Small enough not to be a large burden and large enough for the data set to grow naturally.

##### "We don't have any Data or Cones."
Sharing is caring. This data set lives from your contribution.
If you don't have access to FS Cones we can provide you with raw data.
This way, newer teams get an easy way to buy-in.

If you're interested in accessing this dataset: 
1. [Write us an e-mail](mailto:fsoco@munichmotorsport.de)
1. Upload data to shared Google Photos album
    1. On `Settings` choose `High quality (free unlimited storage)`
1. Fork the repository
1. Add labels to the repository
    1. If your labels use indices for the classes: Add `shortTeamName-classes.txt` to your label directory. See examples at `labels/mms` `labels/elbflorace`
    Please use zero-based indexing as in the examples for ease of integration into existing scripts.
1. Update [documentation](https://ddavid.github.io/fsoco/)
1. [Add relevant scripts to the repository] OPTIONAL but highly encouraged
1. Open pull request

The pictures are saved and shared through a Google Photos account created because of the available free unlimited storage without significant loss of quality.

## Documentation
As we all know, documentation is key for good performance. Please help improve the documentation of this repository if you stumble upon something or if you add scripts.
[The documentation](https://ddavid.github.io/fsoco/) is hosted on [GitHub](https://github.com), based on the `docs/` directory in this repository and uses [Markdown](https://github.github.com/gfm/) to make it as easy as possible to contribute. The landing page is based on `docs/index.md`.

## Support

If you're interested in helping out, contact us: <a href=mailto:fsoco@munichmotorsport.de>fsoco@municHMotorsport.de</a>
