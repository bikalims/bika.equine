# -*- coding: utf-8 -*-

import logging
from zope.i18nmessageid import MessageFactory

PRODUCT_NAME = "bika.equine"
PROFILE_ID = "profile-{}:default".format(PRODUCT_NAME)

# Defining a Message Factory for when this product is internationalized.
bikaEquineMessageFactory = MessageFactory(PRODUCT_NAME)

logger = logging.getLogger(PRODUCT_NAME)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    logger.info("*** Initializing BIKA.EQUINE ***")
