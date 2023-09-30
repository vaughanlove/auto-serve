""" Module for langchain tools
"""
from langchain.tools.base import BaseTool
from langchain.callbacks.manager import CallbackManagerForToolRun
from typing import Optional, Type, List
from pydantic import BaseModel, Field

import json
# import re

#from source.agent.order import Order

#square_order = Order()


# class GetDetailedMenuTool(BaseTool):
#     """Tool for retrieving the menu."""

#     name = "get_detailed_menu_tool"
#     description = "helpful for listing the entire menu when details like size or flavor \
#         of an item are asked about. important** DO NOT USE THIS FOR ORDERING IF SOMEONE IS ASKING FOR THE MENU."
#     args_schema: Type[None] = None

#     def _run(self, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
#         """Get from square api"""
#         nice_menu = []

#         for obj in square_order.menu["objects"]:
#             for variation in obj["item_data"]["variations"]:
#                 temp_item = (
#                     (
#                         variation["item_variation_data"]["name"]
#                         + " "
#                         + obj["item_data"]["name"]
#                     )
#                     .lower()
#                     .replace(",", "")
#                     .replace("(", "")
#                     .replace(")", "")
#                 )
#                 nice_menu.append(temp_item)
#         return nice_menu


# class FindItemIdSchema(BaseModel):
#     name: str = Field(
#         description="The name of a menu item. important** If provided, \
#         include adjectives like size, ie small, medium, or large. \
#         Menu items will usually have adjectives before them like 'small' or 'pumpkin', \
#         make sure to include those."
#     )

class SingleOrder(BaseModel):
    item: str = Field("Name of ordered item.") 
    quantity: str = Field("quantity of ordered item.") 

class OrderSchema(BaseModel):
    order: List[SingleOrder] = Field(description="A order")

def order_run(
        self,
        order: List,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
    print(order)

class OrderTool(BaseTool):
    """Tool for creating and updating orders."""
    name = "order_tool"
    description = """This tool is for creating new orders or adding items to existing
                    orders."""
    args_schema: Type[OrderSchema] = OrderSchema
    func=order_run,


# class FindItemIdTool(BaseTool):
#     """Tool for finding the square id corresponding to the natural language input item"""
#     name = "find_item_id_tool"
#     description = """This tool is for finding the item IDs corresponding to the name of a menu item.
#                     Do not hallucinate.
#                     You should use this tool before using the Order tool.
#                     """
#     args_schema: Type[FindItemIdSchema] = FindItemIdSchema

#     def _run(
#         self, name, run_manager: Optional[CallbackManagerForToolRun] = None
#     ) -> str:
#         """Check the menu for a similar match."""
#         items = []
#         for obj in square_order.menu["objects"]:
#             for variation in obj["item_data"]["variations"]:
#                 temp_item = (
#                     (
#                         variation["item_variation_data"]["name"]
#                         + " "
#                         + obj["item_data"]["name"]
#                     )
#                     .lower()
#                     .replace(",", "")
#                     .replace("(", "")
#                     .replace(")", "")
#                 )
#                 temp_name = (
#                     name.lower()
#                     .replace(",", "")
#                     .replace("(", "")
#                     .replace(")", "")
#                     .split(" ")
#                 )
#                 items.append(temp_item)
#                 same = True
#                 # TOdo replace with regex
#                 for ty in temp_item.split(" "):
#                     same = same & (ty in temp_name)

#                 if same:
#                     return variation["id"]

#         return """The requested item was not found on the menu.
#                 ask the customer to please try ordering again more specifically."""
